# class Elevador:
#     def __init__(self, Limite_pessoas: int, Numero_andares: int):
#         """ 
#         Inicializa o elevador com o limite de pessoas e o n mero de andares.
        
#         Parameters:
#         Limite_pessoas (int): O n mero m ximo de pessoas que o elevador pode suportar.
#         Numero_andares (int): O n mero de andares que o elevador tem.
#         """
#         self.qtd_pessoas = 0 
#         self.limite_pessoas = Limite_pessoas
#         self.andar_atual = 0 
#         self.numero_andares = Numero_andares
        
#     def subir(self):
#         if self.andar_atual < self.numero_andares:
#             self.andar_atual += 1
#             print(f'Subindo -> Andar atual: {self.andar_atual}')   
#         else:
#             print('Você já está no último andar')

#     def entrar(self, qtd: int):
#         if self.qtd_pessoas + qtd <= self.limite_pessoas:
#             self.qtd_pessoas += qtd
#             print(f'Entrando {qtd} pessoas -> Quantidade de pessoas: {self.qtd_pessoas}')
#         else:
#             print('Limite de pessoas excedido')


# elevador1 = Elevador(8, 6)
# elevador2 = Elevador(10, 20)
# elevador3 = Elevador(5, 4)

# print(elevador1.limite_pessoas, elevador1.numero_andares)
# elevador1.andar_atual = 1
# print(elevador1.andar_atual)

# elevador1.subir()
# elevador1.subir()
# elevador1.entrar(5)

# POO - HERANÇA

# class Funcionario:
#     def __init__(self, nome: str, cpf: str, salario: float):
#         """ 
#         Inicializa o Funcionario com o nome, cpf e sal rio.
        
#         Parameters:
#         nome (str): O nome do Funcionario.
#         cpf (str): O cpf do Funcionario.
#         salario (float): O salário do Funcionario.
#         """ 
#         self.nome = nome
#         self.cpf = cpf
#         self.salario = salario
#     def exibir_dados(self):
#         print(f"Nome: {self.nome} - cpf: {self.cpf} - salário: {self.salario}")

# class Professor(Funcionario):
#     def __init__(self, nome: str, cpf: str, salario: float, area: str):
#         super().__init__(nome, cpf, salario)
#         self.area = area

#     def exibir_dados(self):
#         super().exibir_dados()
#         print(f"Área: {self.area}")


# class Diretor(Funcionario):
#     pass

# class Coordenador(Funcionario):
#     pass

# prof1 = Professor("Carlos", "123.456.789-00", 1000000)
# diretor1 = Diretor("Maria", "987.654.321-00", 2000000)
# diretor1.exibir_dados()
# prof1.exibir_dados()


class Veiculo:
    def __init__(self, marca: str, modelo: str, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        

    def exibir_dados(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Cor: {self.cor}")

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str):
        super().__init__(marca, modelo, cor)
        self.celindradas = 160

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Celindradas: {self.celindradas}")

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str,):
        super().__init__(marca, modelo, cor)
        self.portas = 4

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Portas: {self.portas}")

carro1 = Carro("Honda", "Civic", "Prata")
carro1.exibir_dados()
moto1 = Moto("Honda", "CG-Fan160", "Prata")
moto1.exibir_dados()



