from src.cliente.entidade_cliente import Cliente
from src.quarto.entidade_quarto import Quarto
from  datetime import datetime


class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = datetime.now()
        self.checkout = None
        self.status = True
    

    def realizar_checkout(self):
        self.checkout = datetime.now()
        self.status = False
        self.quarto.disponivel = True
        
    def __repr__(self):
        return f"<Reserva: cliente={self.cliente}, quarto={self.quarto}, data_entrada={self.data_entrada}, data_saida={self.data_saida}, status={self.status}>"
        
    


if __name__ == "__main__":
    import time
    cliente1 = Cliente("Lukas", "luk.devjobs@gmail.com", "859 99999999" )
    quarto1 = Quarto(101, "Suite", 500.00, True)
    reserva1 = Reserva(cliente1, quarto1)
    print(reserva1)
        