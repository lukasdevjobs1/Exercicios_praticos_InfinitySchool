import json
from collections import defaultdict, deque
from heapq import nlargest
import time
from typing import List, Dict, Set
import pickle


def save_system(system, filename):
    with open(filename, 'wb') as f:
        pickle.dump(system, f)

def load_system(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

class BookRecommendationSystem:
    def __init__(self):
        # Estruturas de dados principais
        self.books = {}  # Hash Table: book_id -> book_info
        self.users = {}  # Hash Table: user_id -> user_info
        self.user_ratings = defaultdict(dict)  # user_id -> {book_id: rating}
        self.book_ratings = defaultdict(list)  # book_id -> list of ratings
        
        # Grafos para relações
        self.user_similarity_graph = defaultdict(set)  # Grafo de similaridade
        self.book_graph = defaultdict(list)  # Livros similares
        
        # Cache para otimização
        self.recommendation_cache = {}

    def add_book(self, book_id: str, title: str, author: str, genres: List[str]):
        """Adiciona um livro ao sistema usando Hash Table"""
        self.books[book_id] = {
            'title': title,
            'author': author,
            'genres': set(genres),  # Set para busca rápida
            'average_rating': 0.0,
            'rating_count': 0
        }
    
    def add_user(self, user_id: str, name: str, preferred_genres: List[str]):
        """Adiciona um usuário ao sistema"""
        self.users[user_id] = {
            'name': name,
            'preferred_genres': set(preferred_genres),
            'reading_history': deque(maxlen=100)  # Fila para histórico recente
        }
    
    def add_rating(self, user_id: str, book_id: str, rating: int):
        """Adiciona uma avaliação - atualiza múltiplas estruturas"""
        # Atualiza avaliações do usuário (Hash Table)
        self.user_ratings[user_id][book_id] = rating
        
        # Atualiza avaliações do livro (Lista)
        self.book_ratings[book_id].append(rating)
        
        # Atualiza histórico do usuário (Fila)
        self.users[user_id]['reading_history'].append(book_id)
        
        # Recalcula rating médio do livro
        self._update_book_rating(book_id)
        
        # Limpa cache (estratégia de invalidação)
        self.recommendation_cache.pop(user_id, None)
    
    def _update_book_rating(self, book_id: str):
        """Atualiza o rating médio do livro - Algoritmo de média"""
        ratings = self.book_ratings[book_id]
        if ratings:
            average = sum(ratings) / len(ratings)
            self.books[book_id]['average_rating'] = round(average, 2)
            self.books[book_id]['rating_count'] = len(ratings)
    
    def get_similar_users(self, user_id: str, k: int = 5) -> List[str]:
        """Encontra usuários similares usando algoritmo de similaridade por cosine"""
        if user_id not in self.user_ratings:
            return []
        
        user_ratings = self.user_ratings[user_id]
        similarities = []
        
        for other_user_id, other_ratings in self.user_ratings.items():
            if other_user_id == user_id:
                continue
            
            # Calcula similaridade usando cosine similarity
            similarity = self._cosine_similarity(user_ratings, other_ratings)
            if similarity > 0:  # Só considera similaridades positivas
                similarities.append((similarity, other_user_id))
        
        # Usa Heap para pegar os K maiores (algoritmo de seleção)
        most_similar = nlargest(k, similarities)
        return [user_id for _, user_id in most_similar]
    
    def _cosine_similarity(self, ratings1: Dict, ratings2: Dict) -> float:
        """Algoritmo de similaridade por cosine entre dois vetores de ratings"""
        common_books = set(ratings1.keys()) & set(ratings2.keys())
        if not common_books:
            return 0.0
        
        dot_product = sum(ratings1[book] * ratings2[book] for book in common_books)
        magnitude1 = sum(r ** 2 for r in ratings1.values()) ** 0.5
        magnitude2 = sum(r ** 2 for r in ratings2.values()) ** 0.5
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
            
        return dot_product / (magnitude1 * magnitude2)
    
    def recommend_books_collaborative(self, user_id: str, n_recommendations: int = 10) -> List[Dict]:
        """Sistema de recomendação colaborativa baseado em filtragem colaborativa"""
        if user_id in self.recommendation_cache:
            return self.recommendation_cache[user_id]
        
        user_rated_books = set(self.user_ratings[user_id].keys())
        recommendations = defaultdict(float)
        
        # Encontra usuários similares
        similar_users = self.get_similar_users(user_id)
        
        for similar_user in similar_users:
            similarity = self._cosine_similarity(
                self.user_ratings[user_id], 
                self.user_ratings[similar_user]
            )
            
            # Para cada livro que o usuário similar leu e o atual não leu
            for book_id, rating in self.user_ratings[similar_user].items():
                if book_id not in user_rated_books:
                    # Ponderar pelo grau de similaridade
                    recommendations[book_id] += rating * similarity
        
        # Ordena recomendações (algoritmo de ordenação)
        sorted_recommendations = sorted(
            recommendations.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:n_recommendations]
        
        result = []
        for book_id, score in sorted_recommendations:
            book_info = self.books[book_id].copy()
            book_info['recommendation_score'] = round(score, 3)
            book_info['id'] = book_id
            result.append(book_info)
        
        # Cache para otimização
        self.recommendation_cache[user_id] = result
        return result
    
    def recommend_books_content_based(self, user_id: str, n_recommendations: int = 10) -> List[Dict]:
        """Recomendação baseada em conteúdo usando preferências do usuário"""
        if user_id not in self.users:
            return []
        
        user_genres = self.users[user_id]['preferred_genres']
        user_rated_books = set(self.user_ratings[user_id].keys())
        recommendations = []
        
        # Busca linear por livros compatíveis (poderia ser otimizado com índice invertido)
        for book_id, book_info in self.books.items():
            if book_id in user_rated_books:
                continue
                
            # Calcula compatibilidade por gênero
            genre_match = len(user_genres & book_info['genres'])
            if genre_match > 0:
                score = genre_match + (book_info['average_rating'] / 5)
                recommendations.append((score, book_id, book_info))
        
        # Ordena por score (QuickSort internamente)
        recommendations.sort(key=lambda x: x[0], reverse=True)
        
        return [
            {**book_info, 'recommendation_score': score, 'id': book_id}
            for score, book_id, book_info in recommendations[:n_recommendations]
        ]
    
    def search_books(self, query: str, genre: str = None, min_rating: float = 0) -> List[Dict]:
        """Sistema de busca com filtros - usando múltiplos algoritmos de busca"""
        results = []
        query = query.lower()
        
        # Busca linear com filtros (em sistema real, usaríamos índice invertido)
        for book_id, book_info in self.books.items():
            # Filtro por rating
            if book_info['average_rating'] < min_rating:
                continue
            
            # Filtro por gênero
            if genre and genre not in book_info['genres']:
                continue
            
            # Busca no título e autor
            if (query in book_info['title'].lower() or 
                query in book_info['author'].lower()):
                results.append({**book_info, 'id': book_id})
        
        # Ordena por rating (algoritmo de ordenação)
        return sorted(results, key=lambda x: x['average_rating'], reverse=True)
    
    def get_trending_books(self, days: int = 30) -> List[Dict]:
        """Livros em tendência baseado em atividade recente"""
        # Simula análise temporal (em sistema real, teríamos timestamps)
        recent_activity = defaultdict(int)
        
        for user_id, user_info in self.users.items():
            # Usa deque (fila) para histórico recente
            for book_id in user_info['reading_history']:
                recent_activity[book_id] += 1
        
        # Encontra os N mais populares (algoritmo de seleção)
        trending_books = nlargest(10, recent_activity.items(), key=lambda x: x[1])
        
        return [
            {**self.books[book_id], 'id': book_id, 'recent_activity': activity}
            for book_id, activity in trending_books
        ]

# Exemplo de uso prático do sistema
def demo_sistema_recomendacao():
    print("📚 INICIANDO DEMO DO SISTEMA BOOKMATCH\n")
    
    # 1. Inicializa o sistema
    system = BookRecommendationSystem()
    
    # 2. Adiciona livros ao catálogo
    books_data = [
        ("001", "Python para Data Science", "João Silva", ["Tecnologia", "Programação"]),
        ("002", "Machine Learning Básico", "Maria Santos", ["Tecnologia", "IA"]),
        ("003", "O Senhor dos Anéis", "J.R.R. Tolkien", ["Fantasia", "Aventura"]),
        ("004", "1984", "George Orwell", ["Ficção", "Distopia"]),
        ("005", "Clean Code", "Robert Martin", ["Programação", "Tecnologia"]),
        ("006", "Harry Potter", "J.K. Rowling", ["Fantasia", "Aventura"]),
        ("007", "Arquitetura de Software", "Martin Fowler", ["Programação", "Tecnologia"]),
    ]
    
    for book in books_data:
        system.add_book(*book)
    
    # 3. Cadastra usuários
    users_data = [
        ("user1", "Ana", ["Programação", "Tecnologia"]),
        ("user2", "Carlos", ["Fantasia", "Aventura"]),
        ("user3", "Beatriz", ["Tecnologia", "IA", "Programação"]),
    ]
    
    for user in users_data:
        system.add_user(*user)
    
    # 4. Simula avaliações dos usuários
    ratings = [
        ("user1", "001", 5), ("user1", "005", 4), ("user1", "007", 5),
        ("user2", "003", 5), ("user2", "006", 4),
        ("user3", "001", 4), ("user3", "002", 5), ("user3", "005", 3),
    ]
    
    for rating in ratings:
        system.add_rating(*rating)
    
    # 5. Demonstra funcionalidades
    print("1. 🎯 RECOMENDAÇÕES COLABORATIVAS PARA ANA (user1):")
    recommendations = system.recommend_books_collaborative("user1", 3)
    for book in recommendations:
        print(f"   📖 {book['title']} - Score: {book['recommendation_score']}")
    
    print("\n2. 🔍 BUSCA POR LIVROS DE PROGRAMAÇÃO:")
    search_results = system.search_books("python", "Programação", min_rating=4.0)
    for book in search_results:
        print(f"   📖 {book['title']} - Rating: {book['average_rating']}")
    
    print("\n3. 📊 LIVROS EM ALTA:")
    trending = system.get_trending_books()
    for book in trending[:3]:
        print(f"   📖 {book['title']} - Atividade: {book['recent_activity']}")
    
    print("\n4. 👥 USUÁRIOS SIMILARES À :")
    similar_users = system.get_similar_users("user3")
    print(f"   Usuários similares: {similar_users}")

# Análise de Complexidade e Estruturas Utilizadas
def analise_tecnica():
    print("\n" + "="*50)
    print("🔧 ANÁLISE TÉCNICA DAS ESTRUTURAS E ALGORITMOS")
    print("="*50)
    
    analise = """
    ESTRUTURAS DE DADOS UTILIZADAS:
    • Hash Tables (dict): users, books - O(1) para acesso
    • DefaultDict: user_ratings, book_ratings - evita KeyError
    • Set: genres - busca rápida e operações de conjunto
    • Deque: reading_history - fila com tamanho máximo
    • List: book_ratings - armazenamento sequencial
    
    ALGORITMOS IMPLEMENTADOS:
    • Cosine Similarity: cálculo de similaridade entre usuários
    • Filtragem Colaborativa: recomendação baseada em usuários similares
    • Ordenação (sorted/TimSort): ordenação de recomendações
    • Busca Linear: busca por livros (em pequena escala)
    • Algoritmo de Seleção (nlargest): encontrar top N elementos
    
    OTIMIZAÇÕES:
    • Cache: evita recálculo de recomendações
    • Estruturas adequadas: escolha baseada nas operações necessárias
    • Pré-computação: ratings médios calculados uma vez
    """
    
    print(analise)

if __name__ == "__main__":
    demo_sistema_recomendacao()
    analise_tecnica()