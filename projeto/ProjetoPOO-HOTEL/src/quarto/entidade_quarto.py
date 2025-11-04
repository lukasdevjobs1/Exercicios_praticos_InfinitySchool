class Quarto:
    def __init__(self, numero: int, tipo: str, preco: float, disponivel: bool = False):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = disponivel

    def __repr__(self):
        return f"<Quarto: numero={self.numero}, tipo={self.tipo}, preco={self.preco}, disponivel={self.disponivel}>"

if __name__ == "__main__":
    quarto1 = Quarto(101, "Suite", 500.00, True)
    print(quarto1)
     