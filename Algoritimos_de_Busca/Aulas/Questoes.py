# Questão 1º par ou impar

# num = int(input("Digite um número: "))

# def task(num):
#     if num % 2 == 0:
#         return "par"
#     else:
#         return "impar"
# print("O numero digitado é", task(num))

# Questão 2º numeros positivos e negativos


# num = int(input("Digite um número: "))
# def task(num):
#     if num > 0:
#         return "positivo"
#     elif num < 0:
#         return "negativo"
#     else:
#         return "neutro"
# print("O numero digitado é", task(num))

# Questão 3º velocidade limite

# velocidade = int(input("Digite uma velocidade: "))
# limite = 50
# def task(velocidade):
#     if velocidade > 60:
#         return "acima do limite"
#     else:
#         return "dentro do limite"
# print("A velocidade digitada é", task(velocidade))     
# 
# 
# 4º questão imprimir sequencia 0 a 1000
    
# num = []
# def task(num):
#     for i in range(1001):
#         num.append(i)
#     return num
# print(task(num))

# 5º questão imprimir sequencia 0 a 1000 pares

# num = []
# def task(num):
#     for i in range(1001):
#         if i % 2 == 0:
#             num.append(i)
#     return num
# print(task(num))

#6º solicite 10 numeros e imprima se é par ou impar

# num = []
# def task(num):
#    for i in range(10):
#        num = int(input("Digite um número: "))
#        if num % 2 == 0:
#            print("par")
#        else:
#            print("impar")
    
# print(task(num))


# 7º solicite 10 numeros e imprima se eh positivo ou negativo

# num = []

# def task(num):
#     for i in range(10):
#         num = float(input("Digite um número: "))
#         if num > 0:
#             print("positivo")
#         elif num < 0:
#             print("negativo")
#         else:
#             print("neutro")
# print(task(num))

# 8º velocidade limite de 10 veiculos
# velocidade = []
# limite = 50
# def task(velocidade):
#     for i in range(10):
#         velocidade = int(input("Digite uma velocidade: "))
#     if velocidade > 60:
#         print("acima do limite")
#     else:             
#         print("dentro do limite")
# print(task(velocidade))


# 9º quantidade de pares e impares digitados
# def contar_pares_impares():
#     pares = 0
#     impares = 0

#     for i in range(10):
#         num = int(input(f"Digite o número {i+1}: "))
#         if num % 2 == 0:
#             pares += 1
#         else:
#             impares += 1

#     print(f"Quantidade de números pares: {pares}")
#     print(f"Quantidade de números ímpares: {impares}")

# contar_pares_impares()

# 10º maior e menor idade

# maior_idade = 18
# menor_idade = 17
# idade = []
# def task(idade):
#     for i in range(10):
#         idade = int(input("Digite uma idade: "))
#         if idade >= maior_idade:
#             print("maior de idade")
#         else:
#             print("menor de idade")
# print(task(idade))


# 11º solicite 10 numeros e ao final some os numeros digitados
# num = []
# def task(num):
#     soma = 0
#     for i in range(10):
#         num = int(input("Digite um número: "))
#         soma += num
#     print("A soma dos números digitados é:", soma)
# print(task(num))

# 12º Solicite 10 numeros e ao final faça a soma dos numeros pares

# num = []
# def task(num):
#     soma = 0
#     for i in range(10):
#         num = int(input("Digite um número: "))
#         if num % 2 == 0:
#             soma += num
#     print("A soma dos números pares digitados é:", soma)
# print(task(num))

#13º Solicite 10 numeros e ao final adicione a lista 

# list = []

# def task(num):
#     for i in range(10):
#         num = int(input("Digite um número: "))
#         list.append(num)
#     print("A lista digitada é", (list))
# print(task(list))

# 14º Armazene os pares e impares em listas separadas

# pares = []
# impares = []
# def task():
#     for i in range(10):
#         num = int(input("Digite um número: "))
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)
#     print("A lista de pares digitados é", (pares))
#     print("A lista de impares digitados é", (impares))
# task()

# 15º solicite nome, idade e curso e armazene em um dicionario    

# aluno = {}
# def task(aluno):
#     for i in range(1):
#         aluno['nome'] = input("Digite o nome do aluno: ")
#         aluno['idade'] = int(input("Digite a idade do aluno: "))
#         aluno['curso'] = input("Digite o curso do aluno: ")
#     print("Dados do aluno:", aluno)
# task(aluno)


# def cadastrar_aluno(nome, idade, curso):
#     aluno = {
#         'nome': nome,
#         'idade': idade,
#         'curso': curso
#     }
#     print(aluno)

# cadastrar_aluno("lukas", 31,"ADS")
# nome = input("Digite o nome do aluno: ")
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno: ")
# cadastrar_aluno(nome, idade, curso)
