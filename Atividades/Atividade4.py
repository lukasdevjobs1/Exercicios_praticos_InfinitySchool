def media(nums: list[float]) -> float:
    """Calcula a média aritmética de uma lista de números.
    
    Args:
        nums: Lista de números em ponto flutuante.
        
    Returns:
        A média aritmética dos números da lista.
        
    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not nums:
        raise ValueError("Lista não pode estar vazia")
    return sum(nums) / len(nums)


if __name__ == "__main__":
    # Teste 1: Lista com números positivos
    assert media([1.0, 2.0, 3.0]) == 2.0
    
    # Teste 2: Lista com um único número
    assert media([5.0]) == 5.0
    
    # Teste 3: Lista com números negativos e positivos
    assert media([-1.0, 1.0, 0.0]) == 0.0
    
    # Teste 4: Lista vazia deve levantar ValueError
    try:
        media([])
        assert False, "Deveria ter levantado ValueError"
    except ValueError:
        pass
    
    print("Todos os testes passaram!")