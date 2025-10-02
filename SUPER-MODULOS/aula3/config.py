import os 
# pip install sqlalchemy
from  flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = f'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

db = SQLAlchemy()
