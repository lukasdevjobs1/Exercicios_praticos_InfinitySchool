# Solicita ao usuário que insira um número
num = float(input("Insira um número: "))

# Verifica se o número é positivo, negativo ou zero
if num > 0:
    print(f"O número {num} é positivo.")
elif num < 0:
    print(f"O número {num} é negativo.")
else:
    print(f"O número {num} é zero.")