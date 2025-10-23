def diagonal_difference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        primary_sum += arr[i][i]        # Diagonal principal
        secondary_sum += arr[i][n-1-i]  # Diagonal secundária
    
    return abs(primary_sum - secondary_sum)

# Exemplo de uso
matriz = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

resultado = diagonal_difference(matriz)
print(resultado)  # Output: 15