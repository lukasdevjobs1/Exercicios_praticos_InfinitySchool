lista = [2, 4, 6, 8]
numero = int(input("digite um numero: "))
index_resultado = None
for index in range(len(lista)):
    if lista[index] == numero:
        index_resultado = index
        break
    
    print(f"Indice do elemento digitado: {index_resultado}")
    