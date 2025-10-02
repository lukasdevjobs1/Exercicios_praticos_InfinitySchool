# Solicita ao usuário que insira dois números inteiros
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Inicializa a soma dos números pares
soma_pares = 0

# Verifica se o início é maior que o fim e troca os valores se necessário
if inicio > fim:
    inicio, fim = fim, inicio

# Verifica se o intervalo tem apenas números ímpares
if (inicio % 2 != 0) and (fim % 2 != 0):
    print("Não há números pares no intervalo.")
else:
    # Itera sobre todos os números no intervalo
    for num in range(inicio, fim + 1):
        # Verifica se o número é par
        if num % 2 == 0:
            # Soma o número par à soma total
            soma_pares += num

    # Exibe a soma dos números pares
    print("A soma dos números pares no intervalo é:", soma_pares)
