lista = [11, 7, 4, 2]

for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print(f"{lista[j]} e {lista[j + 1]} trocaram de valor")

print(lista)