import sqlite3

conn = sqlite3.connect("MOVIMENTACOES.db")
cursor = conn.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS movimentacoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER NOT NULL,
        usuarios_id INTEGER NOT NULL,
        tipo TEXT NOT NULL CHECK(tipo IN ('ENTRADA', 'SAIDA')),
        quantidade INTEGER NOT NULL,
        valor_unitario REAL DEFAULT 0,
        data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
        observacao TEXT,
        FOREIGN KEY (produto_id) REFERENCES produtos(id),
        FOREIGN KEY (usuarios_id) REFERENCES usuarios(id)
        )
    '''
)

# Criando um índice para buscas por data
cursor.execute('CREATE INDEX IF NOT EXISTS idx_data_movimentacao ON movimentacoes(data_movimentacao);')

conn.commit()
conn.close()

print("Tabela 'movimentacoes' criada e otimizada com sucesso!")
