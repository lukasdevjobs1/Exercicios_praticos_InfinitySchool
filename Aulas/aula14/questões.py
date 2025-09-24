# 1º crie uma lista de numeros, crie uma nova lista contendo apenas os numeros pares.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nova_lista = [

#     num for num in lista if num % 2 == 0
    
#     ]

# print(nova_lista)


# 2º Você possui dados de vendas trimestrais de uma
    # empresa em uma lista. Cada trimestre é representado
    # como uma lista de números, onde cada número
    # representa o valor de vendas de um mês (janeiro a
    # março, abril a junho, julho a setembro e outubro a

    # dezembro).

    # Você deve realizar as seguintes tarefas:
    # Calcule a média de vendas por trimestre.


trimestre_1 = [100,200,400]
trimestre_2 = [200,300,500]
trimestre_3 = [300,400,600]

def calcular_media_vendas(trimestre_1, trimestre_2, trimestre_3):
    media_trimestre_1 = sum(trimestre_1) / len(trimestre_1),
    media_trimestre_2 = sum(trimestre_2) / len(trimestre_2),
    media_trimestre_3 = sum(trimestre_3) / len(trimestre_3),

    return media_trimestre_1, media_trimestre_2, media_trimestre_3


print(calcular_media_vendas(trimestre_1, trimestre_2, trimestre_3))


