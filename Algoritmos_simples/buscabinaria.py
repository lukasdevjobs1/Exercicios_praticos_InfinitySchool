lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

inicio = 0 

meio = len(lista) // 2

fim = len(lista) - 1

index_procurado = None
numero_procurado = int(input("digite um numero: "))

while inicio <= fim:
    
    meio = (inicio + fim) // 2
    if lista[meio] == numero_procurado:
        index_procurado = meio
        break
    
    elif lista[meio] > numero_procurado:
        fim = meio - 1
    elif lista[meio] < numero_procurado:
        inicio = meio + 1
    print(f"index procurado {index_procurado}")
    