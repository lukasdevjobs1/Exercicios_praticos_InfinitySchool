# # 1ª encontre o maior e o menor número em uma lista de números.
# print(':::::BEM VINDO AOS EXERCICIOS DE PYTHON:::::')


# lista = [3, 7, 1, 9, 4]

# maior = max(lista)
# menor = min(lista)

# def numero(maior, menor):
#     for i in lista:
#         return f"O maior número é {maior} e o menor número é {menor}"
# print(numero(maior, menor))


# # 2ª calcule a media de uma lista de números.

# lista_numeros = [10, 20, 30]

# def media(lista_numeros):
#     return sum(lista_numeros) / len(lista_numeros)
# print(f"A média é {media(lista_numeros)}")

# # 3ª verifique se um numero e par ou impar.

# num = int(input("Digite um número: "))
# def par_ou_impar(num):
#     if num % 2 == 0:
#         return f'O número {num} é par.'
#     else:
#         return f'O número {num} é ímpar.'
# print(par_ou_impar(num))

# # 4ª  conta quantos pares tem em uma lista de números.

# lista_numeros = [1, 2, 3, 4, 5, 6]

# def contar_pares(lista_numeros):
#     pares = 0
#     for numero in lista_numeros:
#         if numero % 2 == 0:
#             pares += 1

#     return f'A lista tem {pares} numeros pares.'
# print(contar_pares(lista_numeros))

# # 5ª inverta uma string.

# string = 'Python'
# def inverter_string(string):
#     return string[::-1]
# print(inverter_string(string))

# # 6ª verifique se uma string é um palíndromo.

# string = 'radar'

# def palindromo(string):
#     return string == string[::-1]
# print(palindromo(string))