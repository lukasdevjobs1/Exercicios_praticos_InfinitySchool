def processar_dados(lista):
    resultado = []
    for item in lista:
        if item % 2 == 0:
            resultado.append(item ** 2)
    return resultado


dados = [1, 2, 3, 4, 5]
print(processar_dados(dados))