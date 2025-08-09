# lista = [73, 12, 58, 91, 34, 7, 46, 29, 85, 63]

# pares = []
# for num in lista:
#     if num % 2 == 0:
#         pares.append(num)
# print(pares)


lista = [1, 2, 2, 3, 4, 4, 5, 5, 1]

lista_sem_duplicadas = []

for num in lista:
    if num not in lista_sem_duplicadas:
        lista_sem_duplicadas.append(num)

print(lista_sem_duplicadas)