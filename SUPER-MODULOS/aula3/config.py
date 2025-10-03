import os
from flask_sqlalchemy import SQLAlchemy
# pip install flask_sqlalchemy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"

db = SQLAlchemy()