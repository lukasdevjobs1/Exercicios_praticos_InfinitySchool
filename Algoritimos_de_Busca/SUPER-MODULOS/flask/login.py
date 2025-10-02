from flask import Flask, render_template, request, redirect, url_for #render -> importar o template

app = Flask(__name__)

cadastro_de_usuario = [
    {
        "nome": "nome",
        'email': "email",
        'senha': "senha"
    }
]

@app.route('/login')
def login():
    email = input("Digite seu email cadastrado: ")
    senha = input("Digite sua senha: ")
    
    for cadastro in cadastro_de_usuario:
        if cadastro_de_usuario[email] == email:
            ...
    