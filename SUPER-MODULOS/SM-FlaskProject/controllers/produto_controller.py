# importa modulo para manipulação do Sistema Operacional
import os
from flask import jsonify, render_template, request, redirect, url_for
from config import db
from models.produto_model import Produto
# Garante que o nome do arquivo é seguro para salvar no sistema
from werkzeug.utils import secure_filename

# Página inicial
def home():
    return render_template("index.html", titulo="Home")

# Listar produtos
def listar_produtos():
    produtos = Produto.query.all()
    return render_template("produtos.html", titulo="Lista de Produtos", produtos=produtos)

# Cadastrar produto
def cadastrar_produto():
    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        
        # Recebe a imagem do formulário
        imagem_file = request.files.get("imagem")
        caminho_imagem = None
        if imagem_file:
            filename = secure_filename(imagem_file.filename)
            caminho_imagem = f"images/{filename}"

            # 🔧 Garante que a pasta static/images exista
            os.makedirs(os.path.join("static", "images"), exist_ok=True)

            # Salva a imagem na pasta static/images
            imagem_file.save(os.path.join("static", caminho_imagem))

        # Cria o produto com imagem
        novo_produto = Produto(name=name, price=price, imagem=caminho_imagem)
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for("listar_produtos"))

    return render_template("criar_produto.html")

# Editar produto
def editar_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return render_template("404.html", descErro="Produto não encontrado!")

    if request.method == "POST":
        produto.name = request.form["name"]
        produto.price = float(request.form["price"])

        # Atualiza imagem se enviar uma nova
        imagem_file = request.files.get("imagem")
        if imagem_file:
            filename = secure_filename(imagem_file.filename)
            caminho_imagem = f"images/{filename}"

            # 🔧 Garante que a pasta static/images exista
            os.makedirs(os.path.join("static", "images"), exist_ok=True)

            imagem_file.save(os.path.join("static", caminho_imagem))
            produto.imagem = caminho_imagem

        db.session.commit()
        return redirect(url_for("listar_produtos"))

    return render_template("editar_produto.html", produto=produto)

# Deletar produto
def deletar_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return render_template("404.html", descErro="Produto não encontrado!")

    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for("listar_produtos"))

# Pesquisar produto por texto
def pesquisar_produto():
    # Obtém o termo de busca da query string da url usando o parâmetro 'q' e retornando minúsculas.
    produto = request.args.get("q", "").lower()
    if produto:
        # ilike para busca case-insensitive e f"%{produto}%" para busca parcial nao importando a posicao.
        produtos = Produto.query.filter(Produto.name.ilike(f"%{produto}%")).all()
        return render_template("produtos.html", titulo=f"Resultados para '{produto}'", produtos=produtos)
    return redirect(url_for("listar_produtos"))

# API para listar produtos em JSON
def api_listar_produtos():
    produtos = Produto.query.all()
    # Converte objetos para lista de dicionários
    lista = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "imagem": p.imagem
        }
        for p in produtos
    ]
    return jsonify(lista)