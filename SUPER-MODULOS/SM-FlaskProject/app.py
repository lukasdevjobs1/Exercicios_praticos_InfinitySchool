import os
from flask import Flask
from config import db, DATABASE_URI
from controllers import produto_controller

app = Flask(__name__)
# Define qual o banco de dados usar
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# Desativa o rastreamento de modificações para economizar memória
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configuração para produção
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Inicializa banco
db.init_app(app)

# Rotas do controller de produtos sem Decorators
app.add_url_rule("/", "home", produto_controller.home)
app.add_url_rule("/home", "home", produto_controller.home)

app.add_url_rule("/produtos", "listar_produtos", produto_controller.listar_produtos)
app.add_url_rule("/produtos/cadastro", "cadastrar_produto", produto_controller.cadastrar_produto, methods=["GET", "POST"])
app.add_url_rule("/produtos/editar/<int:id>", "editar_produto", produto_controller.editar_produto, methods=["GET", "POST"])
app.add_url_rule("/produtos/deletar/<int:id>", "deletar_produto", produto_controller.deletar_produto)

# Rota separada para pesquisa de produtos
app.add_url_rule("/produtos/pesquisar", "pesquisar_produto", produto_controller.pesquisar_produto, methods=["GET"])

# Rota de API
app.add_url_rule("/api/produtos", "api_listar_produtos", produto_controller.api_listar_produtos)

# Cria as tabelas em falta no banco com contexto da aplicação
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)