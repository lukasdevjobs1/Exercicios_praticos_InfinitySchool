import os
from flask_sqlalchemy import SQLAlchemy

# pega o caminho absoluto da pasta onde está o arquivo atual
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# monta a string de conexão para o SQLite
DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"

# cria a instância do SQLAlchemy, que vai gerenciar o banco de dados
db = SQLAlchemy()