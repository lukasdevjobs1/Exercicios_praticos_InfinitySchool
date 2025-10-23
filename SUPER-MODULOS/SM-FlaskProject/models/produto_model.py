# Modelo Produto (ORM SQLAlchemy)
from config import db

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    imagem = db.Column(db.String(200))

    # Faz Retornar o objeto como string
    def __repr__(self):
        return f"<Produto {self.name}>"