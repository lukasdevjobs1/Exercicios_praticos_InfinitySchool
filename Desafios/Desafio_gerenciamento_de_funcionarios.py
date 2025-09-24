# Sistema de Gerenciamento de Funcionários
funcionarios = []
proximo_id = 1

def cadastrar_funcionario():
    global proximo_id
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode estar vazio!")
        return
    
    cargo = input("Cargo: ").strip()
    departamento = input("Departamento: ").strip()
    
    while True:
        try:
            salario = float(input("Salário: "))
            if salario > 0:
                break
            print("Salário deve ser positivo!")
        except ValueError:
            print("Digite um valor válido!")
    
    funcionario = {
        'id': proximo_id,
        'nome': nome,
        'cargo': cargo,
        'salario': salario,
        'departamento': departamento,
        'ativo': True
    }
    funcionarios.append(funcionario)
    proximo_id += 1
    print(f"Funcionário {nome} cadastrado com sucesso!")

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    
    for f in funcionarios:
        status = "Ativo" if f['ativo'] else "Inativo"
        print(f"ID: {f['id']} | {f['nome']} | {f['cargo']} | R$ {f['salario']:.2f} | {f['departamento']} | {status}")

def buscar_por_id():
    try:
        id_busca = int(input("Digite o ID: "))
        for f in funcionarios:
            if f['id'] == id_busca:
                status = "Ativo" if f['ativo'] else "Inativo"
                print(f"ID: {f['id']} | {f['nome']} | {f['cargo']} | R$ {f['salario']:.2f} | {f['departamento']} | {status}")
                return
        print("Funcionário não encontrado!")
    except ValueError:
        print("ID deve ser um número!")

def buscar_por_departamento():
    dept = input("Departamento: ").strip()
    encontrados = [f for f in funcionarios if f['departamento'].lower() == dept.lower()]
    
    if not encontrados:
        print("Nenhum funcionário encontrado neste departamento.")
        return
    
    for f in encontrados:
        status = "Ativo" if f['ativo'] else "Inativo"
        print(f"ID: {f['id']} | {f['nome']} | {f['cargo']} | R$ {f['salario']:.2f} | {status}")

def atualizar_salario():
    try:
        id_func = int(input("Digite o ID do funcionário: "))
        for f in funcionarios:
            if f['id'] == id_func:
                novo_salario = float(input(f"Salário atual: R$ {f['salario']:.2f}. Novo salário: "))
                if novo_salario > 0:
                    f['salario'] = novo_salario
                    print("Salário atualizado com sucesso!")
                else:
                    print("Salário deve ser positivo!")
                return
        print("Funcionário não encontrado!")
    except ValueError:
        print("Digite valores válidos!")

def demitir_funcionario():
    try:
        id_func = int(input("Digite o ID do funcionário: "))
        for f in funcionarios:
            if f['id'] == id_func:
                f['ativo'] = False
                print(f"Funcionário {f['nome']} foi demitido.")
                return
        print("Funcionário não encontrado!")
    except ValueError:
        print("ID deve ser um número!")

def relatorio_salarial():
    ativos = [f for f in funcionarios if f['ativo']]
    if not ativos:
        print("Nenhum funcionário ativo.")
        return
    
    salarios = [f['salario'] for f in ativos]
    print(f"Maior salário: R$ {max(salarios):.2f}")
    print(f"Menor salário: R$ {min(salarios):.2f}")
    print(f"Salário médio: R$ {sum(salarios)/len(salarios):.2f}")

def funcionarios_ativos():
    ativos = [f for f in funcionarios if f['ativo']]
    if not ativos:
        print("Nenhum funcionário ativo.")
        return
    
    for f in ativos:
        print(f"ID: {f['id']} | {f['nome']} | {f['cargo']} | R$ {f['salario']:.2f} | {f['departamento']}")

def exportar_dados():
    with open('funcionarios.txt', 'w') as arquivo:
        arquivo.write("=== RELATÓRIO DE FUNCIONÁRIOS ===\n\n")
        for f in funcionarios:
            status = "Ativo" if f['ativo'] else "Inativo"
            arquivo.write(f"ID: {f['id']} | {f['nome']} | {f['cargo']} | R$ {f['salario']:.2f} | {f['departamento']} | {status}\n")
    print("Dados exportados para 'funcionarios.txt'")

def menu():
    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS ===")
        print("1. Cadastrar funcionário")
        print("2. Listar todos")
        print("3. Buscar por ID")
        print("4. Buscar por departamento")
        print("5. Atualizar salário")
        print("6. Demitir funcionário")
        print("7. Relatório salarial")
        print("8. Funcionários ativos")
        print("9. Exportar dados")
        print("10. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            buscar_por_id()
        elif opcao == '4':
            buscar_por_departamento()
        elif opcao == '5':
            atualizar_salario()
        elif opcao == '6':
            demitir_funcionario()
        elif opcao == '7':
            relatorio_salarial()
        elif opcao == '8':
            funcionarios_ativos()
        elif opcao == '9':
            exportar_dados()
        elif opcao == '10':
            print("Sistema encerrado!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()