import os 
from flask import render_template, request, redirect, url_for
from config import db
from models.produto_model import Produto
from werkzeug.utils import secure_filename

def home():
  return render_template('index.html', titulo='Home')

def listar_produtos():
  produtos = Produto.query.all()
  return render_template('produtos.html', titulo='Lista de Produtos', produtos=produtos)

def cadastrar_produto():
  if request.method == 'POST':
    name = request.form['name']
    price = float(request.form['price'])
    
    imagem_file = request.files.get('image')
    caminho_imagem = None
    if imagem_file:
      filename = secure_filename(imagem_file.filename)
      caminho_imagem = f"images/{filename}"
      
      imagem_file.save(os.path.join('static', caminho_imagem))

    novo_produto = Produto(name=name, price=price, image=caminho_imagem)
    db.session.add(novo_produto)
    db.session.commit()
    return redirect(url_for('listar_produtos'))
  return render_template('cadastrar_produto.html', titulo='Cadastrar Produto')
  
def editar_produto(id):
  produto = Produto.query.get(id)
  if not produto:
    return render_template('404.html', descError='Produto não encontrado')
  
  if request.method == 'POST':
    produto.name = request.form['name']
    produto.price = float(request.form['price'])
    
    imagem_file = request.files.get('image')
    if imagem_file:
      filename = secure_filename(imagem_file.filename)
      caminho_imagem = f"images/{filename}"
      
      imagem_file.save(os.path.join('static', caminho_imagem))
      produto.image = caminho_imagem
    db.session.commit()
    return redirect(url_for('listar_produtos'))
  
  return render_template('editar_produto.html', titulo='Editar Produto', produto=produto)


def deletar_produto(id):
  produto = Produto.query.get(id)
  if not produto:
    return render_template('404.html', descError='Produto não encontrado')
  
  db.session.delete(produto)
  db.session.commit()
  return redirect(url_for('listar_produtos'))
