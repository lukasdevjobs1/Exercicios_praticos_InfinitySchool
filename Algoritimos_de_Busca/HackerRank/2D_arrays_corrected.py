def total(i, j, m):
    # Linha superior da ampulheta
    a = m[i-1][j-1] + m[i-1][j] + m[i-1][j+1]
    # Centro da ampulheta  
    b = m[i][j]
    # Linha inferior da ampulheta
    c = m[i+1][j-1] + m[i+1][j] + m[i+1][j+1]
    return a + b + c

if __name__ == '__main__':
    # Lê a matriz 6x6
    arr = []
    for _ in range(6):
        row = list(map(int, input().split()))
        arr.append(row)
    
    # Calcula todas as somas de ampulhetas
    somas = []
    for i in range(1, 5):  # Centro pode estar nas posições 1,2,3,4
        for j in range(1, 5):
            somas.append(total(i, j, arr))
    
    # Imprime a maior soma
    print(max(somas))