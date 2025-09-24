import csv
import os
from datetime import datetime

despesas = []

def validar_data(data_str):
    if not data_str.strip():
        return True
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def adicionar_despesa():
    print("\n--- Adicionar Despesa ---")
    
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            break
        print("Erro: Título é obrigatório!")
    
    while True:
        try:
            valor = float(input("Valor: "))
            if valor > 0:
                break
            print("Erro: Valor deve ser maior que zero!")
        except ValueError:
            print("Erro: Valor deve ser um número válido!")
    
    while True:
        categoria = input("Categoria: ").strip()
        if categoria:
            break
        print("Erro: Categoria é obrigatória!")
    
    while True:
        data = input("Data (AAAA-MM-DD) [opcional]: ").strip()
        if not data or validar_data(data):
            break
        print("Erro: Data deve estar no formato AAAA-MM-DD!")
    
    despesa = {
        "titulo": titulo,
        "valor": valor,
        "categoria": categoria,
        "data": data if data else ""
    }
    
    despesas.append(despesa)
    print("Despesa adicionada com sucesso!")

def listar_despesas():
    print("\n--- Lista de Despesas ---")
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return
    
    for i, despesa in enumerate(despesas, 1):
        data_str = f" - {despesa['data']}" if despesa['data'] else ""
        print(f"{i}. {despesa['titulo']} - R$ {despesa['valor']:.2f} - {despesa['categoria']}{data_str}")

def filtrar_por_categoria():
    print("\n--- Filtrar por Categoria ---")
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return
    
    categorias = sorted(set(d['categoria'] for d in despesas))
    
    print("Categorias disponíveis:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i} - {categoria}")
    
    while True:
        try:
            escolha = int(input("\nEscolha o número da categoria: "))
            if 1 <= escolha <= len(categorias):
                categoria_escolhida = categorias[escolha - 1]
                break
            print(f"Erro: Escolha entre 1 e {len(categorias)}.")
        except ValueError:
            print("Erro: Digite um número válido.")
    
    despesas_filtradas = [d for d in despesas if d['categoria'] == categoria_escolhida]
    
    print(f"\nDespesas da categoria '{categoria_escolhida}':")
    for i, despesa in enumerate(despesas_filtradas, 1):
        data_str = f" - {despesa['data']}" if despesa['data'] else ""
        print(f"{i}. {despesa['titulo']} - R$ {despesa['valor']:.2f}{data_str}")

def total_por_categoria():
    print("\n--- Total por Categoria ---")
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return
    
    categorias = {}
    for despesa in despesas:
        cat = despesa['categoria']
        categorias[cat] = categorias.get(cat, 0) + despesa['valor']
    
    for categoria, total in categorias.items():
        print(f"{categoria}: R$ {total:.2f}")

def total_geral():
    print("\n--- Total Geral ---")
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return
    
    total = sum(despesa['valor'] for despesa in despesas)
    print(f"Total geral: R$ {total:.2f}")

def salvar_arquivo():
    print("\n--- Salvar em Arquivo ---")
    nome_arquivo = input("Nome do arquivo (sem extensão): ").strip()
    if not nome_arquivo:
        nome_arquivo = "despesas"
    
    documentos = os.path.join(os.path.expanduser("~"), "Documents")
    caminho_completo = os.path.join(documentos, nome_arquivo + ".csv")
    
    try:
        with open(caminho_completo, 'w', newline='', encoding='utf-8') as arquivo:
            for despesa in despesas:
                linha = f"{despesa['titulo']};{despesa['valor']};{despesa['categoria']};{despesa['data']}\n"
                arquivo.write(linha)
        print(f"Despesas salvas em '{caminho_completo}' com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def carregar_arquivo():
    print("\n--- Carregar do Arquivo ---")
    while True:
        nome_arquivo = input("Nome do arquivo: ").strip()
        if nome_arquivo:
            break
        print("Erro: Nome do arquivo não pode estar vazio!")
    
    documentos = os.path.join(os.path.expanduser("~"), "Documents")
    caminho_completo = os.path.join(documentos, nome_arquivo)
    
    try:
        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            linhas_carregadas = 0
            linhas_ignoradas = 0
            
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                
                partes = linha.split(';')
                if len(partes) != 4:
                    linhas_ignoradas += 1
                    print(f"Aviso: Linha malformada ignorada: {linha}")
                    continue
                
                try:
                    titulo, valor_str, categoria, data = partes
                    valor = float(valor_str)
                    
                    if not titulo.strip() or not categoria.strip() or valor <= 0:
                        linhas_ignoradas += 1
                        print(f"Aviso: Linha com dados inválidos ignorada: {linha}")
                        continue
                    
                    despesa = {
                        "titulo": titulo,
                        "valor": valor,
                        "categoria": categoria,
                        "data": data
                    }
                    despesas.append(despesa)
                    linhas_carregadas += 1
                    
                except ValueError:
                    linhas_ignoradas += 1
                    print(f"Aviso: Linha com valor inválido ignorada: {linha}")
            
            print(f"Arquivo carregado! {linhas_carregadas} despesas carregadas.")
            if linhas_ignoradas > 0:
                print(f"{linhas_ignoradas} linhas foram ignoradas por estarem malformadas.")
                
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")

def mostrar_menu():
    print("\n=== CONTROLE DE GASTOS PESSOAIS ===")
    print("1. Adicionar despesa")
    print("2. Listar despesas")
    print("3. Filtrar por categoria")
    print("4. Total por categoria")
    print("5. Total geral")
    print("6. Salvar em arquivo")
    print("7. Carregar do arquivo")
    print("8. Sair")

def main():
    while True:
        mostrar_menu()
        
        try:
            while True:
                opcao = input("\nEscolha uma opção (1-8): ").strip()
                
                if opcao in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    break
                print("Opção inválida! Escolha entre 1 e 8.")
            
            if opcao == "1":
                adicionar_despesa()
            elif opcao == "2":
                listar_despesas()
            elif opcao == "3":
                filtrar_por_categoria()
            elif opcao == "4":
                total_por_categoria()
            elif opcao == "5":
                total_geral()
            elif opcao == "6":
                salvar_arquivo()
            elif opcao == "7":
                carregar_arquivo()
            elif opcao == "8":
                print("Saindo do programa...")
                break
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()