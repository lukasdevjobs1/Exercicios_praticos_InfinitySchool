import sqlite3

def criar_tabela():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER DEFAULT 0,
            disponivel BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def obter_proximo_codigo():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(codigo) FROM produtos')
    resultado = cursor.fetchone()[0]
    conn.close()
    return (resultado or 0) + 1

criar_tabela()



banco_de_dados = [
    {
        "codigo": 1,
        "nome": "mouse",
        "categoria": "perifericos",
        "preco": 199.99,
        "estoque": 0,
        "disponivel": False,
    }
]


codigo_anterior = 1

while True:
    print("--- SISTEMA DE GERENCIAMENTO DE PRODUTOS ---")
    print("1 - Para adicionar um novo produto")
    print("2 - Listar todos os produtos")
    print("3 - Buscar produto")
    print("4 - Deletar produto")
    print("5 - Alterar produto")
    print("6 - Adicionar produto ao estoque")
    print("7 - Ativar produto")
    print("8 - Desativar produto")
    print("0 - Para sair do sistema")
    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        codigo_anterior += 1
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produto = {
            "codigo": codigo_anterior,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "estoque": 0,
            "disponivel": False,
        }
        banco_de_dados.append(produto)
        print(f"Produto: {produto['nome']} adicionado com sucesso!")
    elif opcao == "2":
        print("--- PRODUTOS CADASTRADOS ---")
        for produto in banco_de_dados:
            print(f"Código: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Preço: {produto['preco']}")
            print(f"Estoque: {produto['estoque']}")
            print(f"Disponível: {produto['disponivel']}")
            print("-" * 50)
    elif opcao == "3":
        codigo = int(input("Digite o código do produto: "))
        for produto in banco_de_dados:
            if codigo == produto['codigo']:
                print(f"Nome: {produto['nome']}")
                print(f"Categoria: {produto['categoria']}")
                print(f"Preço: {produto['preco']}")
                print(f"Estoque: {produto['estoque']}")
                print(f"Disponível: {produto['disponivel']}")
                break
        else:
            print("Produto não encontrado!")
    if opcao == "4":
        codigo = int(input("Informe o código do produto: "))
        for produto in banco_de_dados:
            if codigo == produto['codigo']:
                banco_de_dados.remove(produto)
                print("Produto removido com sucesso!")
                break
        else:
            print("Produto não encontrado!")      
    elif opcao == "5":
            codigo = int(input("Digite o código do produto: "))
            for produto in banco_de_dados:
                if codigo == produto['codigo']:
                    produto['nome'] = input("Digite o novo nome do produto: ")
                    produto['categoria'] = input("Digite a nova categoria do produto: ")
                    produto['preco'] = float(input("Digite o novo preço do produto: "))
                    print("Produto alterado com sucesso!")
                    break
            else:
                print("Produto não encontrado!")
    elif opcao == "6":
        codigo = int(input("Digite o código do produto: "))
        for produto in banco_de_dados:
            if codigo == produto['codigo']:
                quantidade = int(input("Digite a quantidade a ser adicionada ao estoque: "))
                if quantidade > 0:
                    produto['estoque'] += quantidade
                print("Produto adicionado ao estoque com sucesso!")
                break
    elif opcao == "7":
        codigo = int(input("Digite o código do produto: "))
        for produto in banco_de_dados:
            if codigo == produto['codigo']:
                produto['disponivel'] = True
                print("Produto disponível com sucesso!")
                break
        else:
            print("Produto não encontrado!")

    elif opcao == "8":
        codigo = int(input("Digite o código do produto: "))
        for produto in banco_de_dados:
            if codigo == produto['codigo']:
                produto['disponivel'] = False
                print("Produto indisponível com sucesso!")
                break
        else:
            print("Produto não encontrado!")

    elif opcao == "8":
        codigo = int(input("Digite o código do produto: "))
        for produto in banco_de_dados:
            if produto == banco_de_dados['disponivel']:
                produto['disponivel'] = False
                print("Produto indisponível com sucesso!")
                break
            
    elif opcao == "0":
        print("Você saiu do sistema!")
        break
