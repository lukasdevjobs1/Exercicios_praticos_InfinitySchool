# Dicionário para armazenar produtos e seus preços
produtos = {}

# Loop para cadastrar 5 produtos
for i in range(1, 6):
    print(f"\nCadastro do Produto {i}:")
    
    # Solicita o nome do produto
    nome = input("Nome do produto: ").strip()
    
    # Solicita o preço (validação para garantir que seja um número positivo)
    while True:
        try:
            preco = float(input("Preço (R$): ").strip())
            if preco >= 0:
                break
            else:
                print("O preço deve ser positivo!")
        except ValueError:
            print("Digite um valor numérico válido!")
    
    # Armazena no dicionário
    produtos[nome] = preco

# Calcula o total somando todos os preços
total = sum(produtos.values())

# Exibe os produtos e o total
print("\n--- RESUMO DA COMPRA ---")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

print(f"\nTOTAL: R$ {total:.2f}")