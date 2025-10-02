def soma_media(lista):
    """
    Esta função recebe uma lista de números e retorna a soma e a média dos números.
    
    :param lista: Lista de números
    :return: Tupla contendo a soma e a média dos números
    """
    if not lista:
        return 0, 0.0
    
    soma = sum(lista)
    media = soma / len(lista)
    
    return soma, media

# Exemplo de uso da função
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))
nota3 = float(input("Digite a segunda nota: "))

soma_media_resultado = soma_media([nota1, nota2, nota3])
print(f"Soma: {soma_media_resultado[0]}, Média: {soma_media_resultado[1]}")
