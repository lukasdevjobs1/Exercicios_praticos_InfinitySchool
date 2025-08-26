# Dicionário para armazenar informações do contato
contato = {}

print("\n--- Cadastro de Contato ---")

# Solicitando e armazenando os dados
contato['nome'] = input("Digite o nome do contato: ")
contato['telefone'] = input("Digite o número de telefone: ")
contato['email'] = input("Digite o endereço de email: ")

# Exibindo os dados de forma organizada
print("\n--- Informações do Contato Cadastrado ---")
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")