result = []
    

    
def removable_indices(str1, str2):


    
    for i in range(len(str1)):
        if str1[:i] + str1[i+1:] == str2:
            result.append(i)
    
        return result if result else [-1]

# Exemplo de uso
if __name__ == "__main__":
    # Teste 1
    print(removable_indices("bcda", "bcd"))  # [3]
    
    # Teste 2
    print(removable_indices("abcda", "abcd"))  # [4]
    
    # Teste 3
    print(removable_indices("xyz", "abc"))  # [-1]

"""
    Encontra todos os índices que podem ser removidos de str1 para formar str2.
    
    Args:
        str1 (str): String original
        str2 (str): String alvo após remoção
    
    Returns:
        list: Lista de índices removíveis ou [-1] se nenhum encontrado
    """