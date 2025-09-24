# crie uma função que solicite um numero por parametro e imprima a sequencia de 0 ate o numero digitado
num = int(input("Digite um número: "))

for i in range(num, -1, -1):
    print(i)