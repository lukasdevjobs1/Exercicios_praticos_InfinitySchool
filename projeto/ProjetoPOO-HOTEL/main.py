# MENUS HOTEL 
from src.cliente.entidade_cliente import Cliente
from src.quarto.entidade_quarto import Quarto

from  datetime import datetime


clientes = []
quartos = []
reservas = []

def menu_cliente():
    while True:
        print("---- MENU CLIENTE ----")
        print("1. Cadastrar cliente")
        print("2. Editar cliente")
        print("3. remover cliente")
        print("4. Listar clientes")
        print("5. buscar cliente")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            cliente = Cliente(nome, email, telefone)
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")


def menu_quarto():
            while True:
                print("---- MENU QUARTO ----")
                print("1. Cadastrar quarto")
                print("2. Editar quarto")
                print("3. remover quarto")
                print("4. Listar quartos")
                print("5. buscar quarto")
                print("6. Sair")

                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    numero = int(input("Digite o numero do quarto: "))
                    tipo = input("Digite o tipo do quarto: ")
                    preco = float(input("Digite o preco do quarto: "))
                    quarto = Quarto(numero, tipo, preco)
                    quartos.append(quarto)
                    print("Quarto cadastrado com sucesso!")
                elif opcao == "6":
                    break
                else:
                    print("Opção inválida!")

        
menu_cliente()
menu_quarto()





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
        return f"<Reserva: cliente={self.cliente}, quarto={self.quarto}, check_in={self.check_in}, check_out={self.checkout}, status={self.status}>"
        
    


if __name__ == "__main__":
    import time
    cliente1 = Cliente("Lukas", "luk.devjobs@gmail.com", "859 99999999" )
    quarto1 = Quarto(101, "Suite", 500.00, True)
    reserva1 = Reserva(cliente1, quarto1)
    print(reserva1)
        