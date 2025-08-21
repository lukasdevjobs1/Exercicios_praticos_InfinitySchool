def maior_numero(a, b, c):
    """Retorna o maior número entre três números."""
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(maior_numero(5, 2, 8))