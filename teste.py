def f(x):
    """
    Função recursiva que retorna 1 se x for maior que 0, ou 0 se x for 0.
    A função utiliza recursão e operadores lógicos para decidir o retorno:
    - Se x != 0: avalia f(x-1) (chamada recursiva), mas sempre retorna 1 para x>0.
    - Se x == 0: retorna 0.

    Exemplos:
        f(3) -> 1
        f(0) -> 0
    """
    return x and f(x -1) or x
print(f(3))


