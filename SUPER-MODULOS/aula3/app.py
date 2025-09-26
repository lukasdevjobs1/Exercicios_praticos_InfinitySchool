from flask import Flask
from config import db, DATABASE_URI 
from controller import produto_controller

app = flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URI'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# ROTAS 
app.add_url_rule("/", "home", produto_controller.home)
app.add_url_rule("/home", "home", produto_controller.home)
app.add_url_rule("/produtos", "listar_produtos", produto_controller.listar_produtos)
app.add_url_rule("/cadastrar-produto", "cadastrar_produto", produto_controller.cadastrar_produto, methods=["GET", "POST"])
app.add_url_rule("/editar-produto/<int:id>", "editar_produto", produto_controller.editar_produto, methods=["GET", "POST"])
app.add_url_rule("/deletar-produto/<int:id>", "deletar_produto", produto_controller.deletar_produto)

with app.app_context():
  db.create_all()
  
if __name__ == "__main__":
  app.run(debug=True)
