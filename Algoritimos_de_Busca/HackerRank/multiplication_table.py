def multiplication_table(n):
    """Imprime a tabuada de multiplicação para o número n"""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Exemplo de uso
if __name__ == '__main__':
    n = int(input())
    multiplication_table(n)