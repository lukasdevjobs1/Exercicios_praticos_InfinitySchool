class Cliente:
    ID = 1 # variavl estática
    def __init__(self, nome: str, telefone: str, email: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        Cliente.ID += 1
        self.id = Cliente.ID


    def __repr__(self):
        return f"<Cliente: id={self.id}, nome={self.nome}, telefone={self.telefone}, email={self.email}>"   
    

if __name__ == "__main__":
    cliente1 = Cliente("Lukas", "luk.devjobs@gmail.com", "859 99999999" )
    print(cliente1)