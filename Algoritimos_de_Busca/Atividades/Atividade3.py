def to_int(valor: str) -> int:
    try:
        return int(valor.strip())
    except ValueError:
        raise ValueError("valor invalido")

def main():
    casos_teste = ["42", "7", "4.2", "abc", "", "  "]
    
    for caso in casos_teste:
        try:
            resultado = to_int(caso)
            print(f"'{caso}' -> {resultado}")
        except ValueError as e:
            print(f"'{caso}' -> Erro: {e}")
    
    print("\nTeste seu próprio valor:")
    valor = input("Digite um valor: ")
    try:
        resultado = to_int(valor)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()