#  Projeto agenda

agenda = {
    "maria": "85 99243-1234",
    "joao": "85 99243-1234",
    "pedro": "85 99243-1234",
    "jose": "85 99243-1234",
    }

while True:
    print(" 1 - Adicionar um contato")
    print("s - Para sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        agenda[nome] = telefone
        print("Contato adicionado com sucesso!")
    elif opcao.lower() == "s":
        break

