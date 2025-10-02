def criar_dicionario():
    """
    Cria um dicionário com algumas informações.

    Returns:
        dict: O dicionário com as informações.
    """

    pessoa = {
    "nome": "lukas",
    "idade": 31,
    "cidade": "fortaleza"
    
}

    print(pessoa["nome"])

    print(pessoa.get("idade"))

