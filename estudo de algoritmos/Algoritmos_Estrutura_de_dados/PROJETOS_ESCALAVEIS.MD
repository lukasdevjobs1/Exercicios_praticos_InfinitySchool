# 🚀 Escalabilidade em Sistemas Reais

## Netflix/Spotify (Milhões de usuários)

```python
# Problema: 200M usuários × 10M itens = 2×10^15 combinações possíveis
# Solução: Estruturas otimizadas + algoritmos inteligentes

# Matrix Factorization com Sparse Arrays
user_factors = sparse_matrix(users=200M, factors=100)  # O(200M × 100)
item_factors = sparse_matrix(items=10M, factors=100)   # O(10M × 100)
# Reduz de 2×10^15 para 2×10^10 operações!
```

## Amazon (Recomendações em tempo real)

```python
# Distributed Hash Tables
user_data = {
    "shard_1": users[0:50M],      # Servidor 1
    "shard_2": users[50M:100M],   # Servidor 2
    "shard_3": users[100M:150M],  # Servidor 3
}

# Bloom Filters para "já viu este produto?"
bloom_filter = BloomFilter(capacity=1B, error_rate=0.1%)  # 1GB vs 100GB
```

=============================================================================================================

# 🧠 Algoritmos Avançados que Você Pode Estudar

## 1. Locality Sensitive Hashing (LSH)

```python
# Encontra usuários similares em O(log n) em vez de O(n²)
def lsh_similarity(user_vector):
    hash_buckets = []
    for i in range(num_hash_functions):
        bucket = hash_function_i(user_vector)
        hash_buckets.append(bucket)
    return similar_users_in_same_buckets(hash_buckets)
```

## 2. MinHash para Similaridade de Conjuntos

```python
# Compara gêneros/preferências rapidamente
def jaccard_similarity_fast(set1, set2):
    # O(1) em vez de O(|set1| + |set2|)
    return minhash1.jaccard(minhash2)
```

## 3. Consistent Hashing (Distribuição)

```python
# Como o sistema cresce de 3 para 100 servidores sem reprocessar tudo
ring = ConsistentHashRing()
ring.add_server("server_1")
ring.add_server("server_2")
# Apenas 1/n dos dados precisa ser movido quando adiciona servidor
```

=============================================================================================================

# 📊 Estruturas de Dados Avançadas

## Trie para Busca de Títulos

```python
class BookTrie:
    # Autocomplete em O(k) onde k = tamanho da query
    def search_prefix(self, prefix):
        return self.get_all_words_with_prefix(prefix)
```

## Segment Trees para Rankings Dinâmicos

```python
# Atualiza ratings e mantém top-K em O(log n)
segment_tree.update(book_id, new_rating)
top_books = segment_tree.query_range_max(0, n, k=10)
```

## Skip Lists para Ordenação Probabilística

```python
# Alternativa a árvores balanceadas, mais simples
skip_list.insert(rating, book_id)  # O(log n) esperado
top_rated = skip_list.get_top_k(10)
```

=============================================================================================================

# 💡 Conceito Mental Chave

> **"Cada estrutura de dados resolve um problema específico de performance"**

- **Hash Table**: "Preciso acessar dados por chave rapidamente"
- **Heap**: "Preciso sempre do maior/menor elemento"
- **Trie**: "Preciso buscar por prefixos"
- **Graph**: "Preciso modelar relacionamentos"
- **Bloom Filter**: "Preciso saber se algo NÃO existe"
