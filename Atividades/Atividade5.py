from typing import List, Dict

def calcular_media(nums: List[float]) -> float:
    """Calcula a média de uma lista de números."""
    return sum(nums) / len(nums)

def resumo(notas: List[float]) -> Dict[str, float]:
    """
    Calcula soma e média das notas.
    
    Args:
        notas: Lista de notas
        
    Returns:
        Dict com 'soma' e 'media'
        
    Raises:
        ValueError: Se lista estiver vazia
    """
    if not notas:
        raise ValueError("Lista não pode estar vazia")
    
    s = sum(notas)
    m = calcular_media(notas)
    return {'soma': s, 'media': m}

if __name__ == "__main__":
    # Teste 1: Lista normal
    print(resumo([8.0, 7.5, 9.0]))
    
    # Teste 2: Lista com um elemento
    print(resumo([10.0]))
    
    # Teste 3: Lista vazia (deve gerar erro)
    try:
        resumo([])
    except ValueError as e:
        print(f"Erro esperado: {e}")