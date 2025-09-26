from config import db

class Produto(db.Model):
  ___tablename__ = 'produtos'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100), nullable=False)
  price = db.Column(db.Float, nullable=False)
  image = db.Column(db.String(200))
  
def __ref__(self):
  return '<Produto {self.name}>'