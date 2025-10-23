def verificar_numero(num):
    """
    Verifica se um número é positivo, negativo ou zero.

    Args:
        num (int): O número a ser verificado.

    Returns:
        None
    """

    if num > 0:
        print("O número é positivo")
    elif num < 0:
        print("O número é negativo")
    else:
        print("O número é zero")

print(verificar_numero(10))

def calcular_media(*args):
    """
    Calcula a média de uma sequência de números.

    Args:
        *args (int): Os números para calcular a média.

    Returns:
        float: A média dos números.
    """    

    if not args:
        return 0
    return sum(args) / len(args)

print(calcular_media(1, 2, 3, 4, 5))



def exibir_dados(**kwargs):
    """
    Exibe os dados de uma pessoa.

    Args:
        **kwargs (dict): Os dados da pessoa.

    Returns:
        None
    """

    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Lukas", idade=31, cidade="Fortaleza")
