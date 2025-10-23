
from flask import Flask, jsonify, request
from book_recommendation_system import BookRecommendationSystem, load_system
import os

app = Flask(__name__)

# Tenta carregar um sistema existente ou cria um novo
system_file = 'book_system.pkl'
if os.path.exists(system_file):
    system = load_system(system_file)
else:
    system = BookRecommendationSystem()

@app.route('/recommend/<user_id>')
def recommend(user_id):
    try:
        # Obtém o número de recomendações da query string (padrão: 10)
        n_recommendations = request.args.get('n', default=10, type=int)
        
        # Obtém as recomendações
        recommendations = system.recommend_books_collaborative(user_id, n_recommendations)
        return jsonify({
            'status': 'success',
            'recommendations': recommendations
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)