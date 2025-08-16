# Desafio de agenda telefônica em Python

agenda = {}

while True:
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Alterar contato")
    print("4. Exibir contatos")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")
        # Adicionar contato
    if opcao == "1":
        nome = input("Digite o nome do contato:")
        telefone = input("Digite o telefone do contato:")
        agenda[nome] = cadastro = {"telefone": telefone}
        print(f"Contato {nome} adicionado com sucesso!")
        # Buscar contato
    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja buscar:")
        if nome in agenda:
            print(f"Nome: {nome}")
            print(f"Telefone: {agenda[nome]['telefone']}")
        else:
            print(f"Contato {nome} nao encontrado!")
            # Alterar contato
    elif opcao == "3":
        nome = input("Digite o nome do contato que deseja alterar:")
        if nome in agenda:
            novo_telefone = input("Digite o novo telefone:")
            agenda[nome]['telefone'] = novo_telefone
            print(f"Contato {nome} alterado com sucesso!")
        else:
            print(f"Contato {nome} nao encontrado!")
    elif opcao == "4":
        # Exibir todos os contatos
        if agenda:
            print("Lista de contatos:")
            for nome, cadastro in agenda.items():
                print(f"Nome: {nome}")
                print(f"Telefone: {cadastro['telefone']}")
                print()
            else:
                print("Nenhum contato na agenda.")

    elif opcao == "5":
        break
    else:
        print("Opcao invalida! Tente novamente.")