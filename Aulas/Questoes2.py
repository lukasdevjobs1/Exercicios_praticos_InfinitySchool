# lista = ["mouse", "teclado", "monitor"]
# print(lista[0])

# lista[0] = "computador"

# print(len(lista))

# lista.append("cadeira")

# print(lista)

# lista.insert(1, "cadeira")
# print(lista)

# lista.pop(1)
# print(lista)

# conjunto = {"mouse", "teclado", "monitor", "mouse", "gabinete", "cadeira"}

# print(conjunto)

# conjunto_vazio = set()
# print(conjunto_vazio)

# lista = ["mouse", "teclado", "monitor", "mouse", "gabinete", "cadeira"]
# sem_duplicados = set(lista)
# lista = list(sem_duplicados)
# print(sem_duplicados)

# carrinho1 = {"mouse", "teclado", "monitor"}
# carrinho2 = {"mouse", "cadeira", "gabinete"}

# carrinho1.update(carrinho2)

# print(carrinho1)

# if "placa mae" in carrinho1:
#     print("Existe!")
# else:
#     print("Não existe!")

# for item in carrinho1:
#     print(item)

# carrinho1.discard("placa mae")
# print(carrinho1)


"""

QUESTÃO 1º

"""


# meu_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# pares = 0
# impares = 0

# for num in meu_set:
#     if num % 2 == 0:
#         print(num)

# for valor in meu_set:
#     if valor % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print(f"Pares: {pares}")
# print(f"Ímpares: {impares}")

# print("total da soma: ", sum(meu_set))


"""
QUESTÃO 2º

"""
# lista2 = [1,1,2,2,3,4,4,5,6]

# sem_duplicados = set(lista2)
# lista2 = list(sem_duplicados)
# print(sem_duplicados)



"""

DICIONARIOS 

"""


# agenda = {
# "jonas": "85 99243-1234",
# "joao": "85 99243-1234",
# "maria": "85 99243-1234",
# }
# print(agenda["maria"])
# agenda["jonas"] = "85 9924-3333" # atualizando o valor de um item
# print(agenda)
# # agenda["maria"] = input("Digite o telefone de Maria: ")
# # print(agenda)
# agenda["julio"] = "31 99243-1234"
# print(agenda)

# nome = input("Digite o nome: ")
# telefone = input("Digite o telefone: ")

# agenda[nome] = telefone
# print(agenda)

agenda = {
"nome": "lukas",
"idade": 31,
"altura": 1.89,
}
print(agenda)






