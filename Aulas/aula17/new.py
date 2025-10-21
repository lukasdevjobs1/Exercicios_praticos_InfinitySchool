'''def indicador_triangulo(lista):
    """
    Verifica se três valores formam um triângulo.
    
    Args:
        lados: lista com três valores numéricos
    
    Returns:
        'Sim' se formam um triângulo, 'Não' caso contrário
    """
    a, b, c = lista
    
    # Verifica a condição de existência do triângulo
    if (a < b + c) and (b < a + c) and (c < a + b):
        return 'Sim'
    else:
        return 'Não'

# Exemplos de uso
print(indicador_triangulo([2, 2, 5]))  # Saída: Não
print(indicador_triangulo([3, 3, 5]))  # Saída: Sim
print(indicador_triangulo([5, 5, 5]))  # Saída: Sim
print(indicador_triangulo([1, 2, 3]))  # Saída: Não '''




'''def media_aproveitamento(lista):
    
    n1, n2, n3, media_exercicios = lista
    
 
    media_aproveitamento = (n1 * 1 + n2 * 2 + n3 * 3 + media_exercicios) / 7
    
 
    if media_aproveitamento >= 9.0:
        return "A"
    elif media_aproveitamento >= 7.5:
        return "B"
    elif media_aproveitamento >= 6.0:
        return "C"
    else:
        return "D"


print(media_aproveitamento([2, 5, 8, 6]))
print(media_aproveitamento([10, 10, 10, 10]))
print(media_aproveitamento([5, 7.5, 8.5, 8]))


print("\nVerificação dos cálculos:")
print(f"[2,5,8,6]: {(2*1 + 5*2 + 8*3 + 6) / 7}")      
print(f"[10,10,10,10]: {(10*1 + 10*2 + 10*3 + 10) / 7}")
print(f"[5,7.5,8.5,8]: {(5*1 + 7.5*2 + 8.5*3 + 8) / 7}") '''



brian = ('a','b','c') / 3 = 8 

print(brian)

