import sqlite3 

conn = sqlite3.connect("loja219.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL,
        EMAIL TEXT UNIQUE NOT NULL,
        SENHA TEXT NOT NULL,
        TIPO TEXT DEFAULT "operador",
        ATIVO INTEGER DEFAULT 1,
        DATA_CADASTRO DATETIME DEFAULT CURRENT_TIMESTAMP
               
    )
               
    ''')

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        descricao TEXT 
    )
    ''')


cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        codigo_barras TEXT UNIQUE,
        categoria_id INTEGER,
        preco_compra REAL DEFAULT 0,
        preco_venda REAL DEFAULT 0,
        estoque_minimo INTEGER DEFAULT 0,
        estoque_atual INTEGER DEFAULT 0,
        unidade_medida TEXT DEFAULT "UN",
        ativo INTEGER DEFAULT 1,
        data_cadastro  DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)    
    )
    ''')

def adicionar_usuario(nome, email, senha):
    cursor.execute("""
            INSERT INTO usuarios (nome, email, senha),
            VALUES (?, ?, ?)
""", (nome, email, senha))
    conn.commit()


def adicionar_categoria(nome, descricao):
    cursor.execute("INSERT INTO categorias (nome, descricao) VALUES (?,?)", (nome, descricao))
    conn.commit()


def adicionar_produto(nome, descricao, categoria_id, codigo_barras):
    cursor.execute("""
                INSERT INTO produtos (nome, descricao, categoria_id, codigo_barras)
                VALUES (?,?,?,?)
                """, (nome, descricao, categoria_id, codigo_barras))
    conn.commit()

cursor.execute("""
    SELECT produtos.id, produtos.nome, produtos.descrição, categorias.nome
    FROM produtos
    INNER JOIN categorias ON produtos.categorias_id = categorias.id
    """)
produtos = cursor.fetchall()
print(produtos)