from flask import Flask, render_template, request, redirect, url_for 

app = Flask(__name__) 

# ========== API REST ENDPOINTS ==========

# GET /api/produtos - Listar todos os produtos
@app.route('/api/produtos', methods=['GET'])
def api_listar_produtos():
    return jsonify(get_produtos_list())

# GET /api/produtos/<id> - Obter produto específico
@app.route('/api/produtos/<int:id>', methods=['GET'])
def api_obter_produto(id):
    produto = produtos_dict.get(id)
    if produto is None:
        return jsonify({'error': 'Produto não encontrado'}), 404
    return jsonify(produto)

# POST /api/produtos - Criar novo produto
@app.route('/api/produtos', methods=['POST'])
def api_criar_produto():
    data = request.get_json()
    if not data or 'name' not in data or 'preco' not in data:
        return jsonify({'error': 'Dados inválidos'}), 400
    
    novo_id = max(produtos_dict.keys(), default=0) + 1
    novoproduto = {
        'id': novo_id,
        'name': data['name'],
        'preco': float(data['preco'])
    }
    produtos_dict[novo_id] = novoproduto
    return jsonify(novoproduto), 201

# PUT /api/produtos/<id> - Atualizar produto
@app.route('/api/produtos/<int:id>', methods=['PUT'])
def api_atualizar_produto(id):
    if id not in produtos_dict:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    
    produto = produtos_dict[id]
    if 'name' in data:
        produto['name'] = data['name']
    if 'preco' in data:
        produto['preco'] = float(data['preco'])
    
    return jsonify(produto)

# DELETE /api/produtos/<id> - Deletar produto
@app.route('/api/produtos/<int:id>', methods=['DELETE'])
def api_deletar_produto(id):
    if id not in produtos_dict:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    del produtos_dict[id]
    return jsonify({'message': 'Produto deletado com sucesso'}), 200


# Dicionário para busca O(1) por ID
produtos_dict = {
    1: {"id": 1, "name": "camisa", "preco": 49.90},
    2: {"id": 2, "name": "sapato", "preco": 349.90},
    3: {"id": 3, "name": "calça", "preco": 149.90}
}

# Função para obter lista de produtos (compatibilidade com templates)
def get_produtos_list():
    return list(produtos_dict.values())


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', titulo="Home")

@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', titulo="Lista de Produtos", produtos=get_produtos_list())

@app.route('/produtos/cadastro', methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == 'POST':
        novo_id = max(produtos_dict.keys(), default=0) + 1
        novoproduto = {
            'id': novo_id,
            'name': request.form['nome'],
            'preco': float(request.form['preco'])
        }
        produtos_dict[novo_id] = novoproduto
        return redirect(url_for('listar_produtos'))
    return render_template('cadastro_produto.html')

@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = produtos_dict.get(id)
    if produto is None:
        return render_template('404.html', descErro="Produto Não Encontrado!")
    if request.method == 'POST':
        produto['name'] = request.form['name']
        produto['preco'] = float(request.form['preco'])
        return redirect(url_for('listar_produtos'))
    return render_template('editar_produto.html', produto=produto)
    

@app.route('/produtos/deletar/<int:id>')
def deletar_produto(id):
    if id not in produtos_dict:
        return render_template('404.html', descErro='Produto não encontrado!')
    del produtos_dict[id]
    return redirect(url_for('listar_produtos'))

if __name__ == '__main__':
    import os
    os.environ['FLASK_SKIP_DOTENV'] = '1'
    app.run(debug=True)