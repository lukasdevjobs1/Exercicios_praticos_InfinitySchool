## aqui vamos criar a nossa funcao ##
def media(num1, num2, num3):
    soma = num1 + num2 + num3
    media_aritmetica = soma / 3
    return media_aritmetica

## aqui vamos chamar a funcao ## 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media_aritmetica = media(num1, num2, num3)
print("A média aritmética dos números digitados é:", media_aritmetica)