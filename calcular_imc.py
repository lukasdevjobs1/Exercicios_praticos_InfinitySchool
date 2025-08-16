def calcular_imc(peso: float, altura: float) -> dict[str, float | str]:
    """
    Calcula o IMC e retorna a categoria segundo a OMS.
    
    Args:
        peso: Peso em kg (deve ser > 0)
        altura: Altura em metros (deve ser > 0)
    
    Returns:
        Dict com 'imc' (float) e 'categoria' (str)
    
    Raises:
        ValueError: Se peso ou altura <= 0
    """
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero")
    
    imc = round(peso / (altura ** 2), 2)
    
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return {"imc": imc, "categoria": categoria}


if __name__ == "__main__":
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    resultado = calcular_imc(peso, altura)
    print(f"IMC: {resultado['imc']}, Categoria: {resultado['categoria']}")