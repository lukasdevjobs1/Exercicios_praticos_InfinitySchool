import os

# Teste do caminho para a pasta Documentos
documentos = os.path.join(os.path.expanduser("~"), "Documents")
print(f"Pasta Documentos: {documentos}")
print(f"Pasta existe: {os.path.exists(documentos)}")

# Teste de criação de arquivo
nome_arquivo = "teste_despesas.csv"
caminho_completo = os.path.join(documentos, nome_arquivo)
print(f"Caminho completo: {caminho_completo}")

try:
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("titulo;valor;categoria;data\n")
        arquivo.write("Teste;100.50;alimentacao;2024-01-15\n")
    print("Arquivo criado com sucesso!")
    
    # Verificar se o arquivo foi criado
    if os.path.exists(caminho_completo):
        print("Arquivo confirmado na pasta Documentos!")
        
        # Ler o arquivo para confirmar o conteúdo
        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo:\n{conteudo}")
    else:
        print("Erro: Arquivo não foi encontrado!")
        
except Exception as e:
    print(f"Erro: {e}")