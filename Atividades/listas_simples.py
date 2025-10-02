lista= [1,2,3,4,5,6,7,8,9,10]

pares = 0
impares = 0
menores_que_5 = 0


for lista in range(10):
    if lista % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if lista < 5:
        menores_que_5 += 1

        print(f"Quantidade de pares: {pares}")
        print(f"Quantidade de ímpares: {impares}")
        print(f"Quantidade de números menores que 5: {menores_que_5}")