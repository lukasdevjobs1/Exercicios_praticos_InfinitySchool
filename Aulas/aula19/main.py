# # POO II - asssociação e encapsulamento

# class Autor:
#     def __init__(self, nome: str, sobrenome: str, ano_nascimento: int):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.ano_nascimento = ano_nascimento
        
#     def __repr__(self):
#         return f"<Autor: ({self.nome}, {self.sobrenome}, {self.ano_nascimento})>"
    
# class Livro:
#     def __init__(self, cod: int, titulo: str, autor: Autor, estoque: int):
#         self.codigo = cod
#         self.titulo = titulo
#         self.autor = autor
#         self.estoque = estoque


# autor = Autor("Robert", "Jacobina", 2002)
# print(autor)
# book = Livro(1, "harry potter", autor, 2)
# print(book.codigo)
# print(book.titulo)
# print(book.autor)
# print(book.autor.nome)
# print(book.autor.sobrenome)
# print(book.autor.ano_nascimento)
# print(book.estoque)


# # ativide 1ª Crie uma classe chamada Motor com os atributos
# class Motor:
#     def __init__(self, tamanho, numero_valvulas, tipo, ligado: bool):
#         self.ligado = ligado
#         self.tamanho = tamanho
#         self.numero_valvulas = numero_valvulas
#         self.tipo = tipo
#         self.ligado = True

#     def ligar(self):
#         self.ligado = True
#     def desligar(self):
#         self.ligado = False

# # crie uma classe chamada Carro com os atributos
# class carro():
#     def __init__(self, motor: Motor, marca: str, modelo: str, cor: str):
#         self.marca = marca
#         self.modelo = modelo
#         self.cor = cor
#         self.motor = motor
#         self.motor.ligado = True


# # crie um objeto da classe carro e exiba seus atributos

# carro1 = carro(Motor(2.0, 4, "gasolina", True), "Honda", "Civic", "Prata")
# print(carro1.motor.ligado)
# print(carro1.motor.tamanho)
# print(carro1.motor.numero_valvulas)
# print(carro1.motor.tipo)




class Pessoa:
    def __init__(self, nome: str, idade: int, sobrenome: str):
        self.__nome = nome
        self.__idade = idade
        self.__sobrenome = sobrenome

    def get_nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            Print("Erro! O nome deve ser uma string")

    def set_nome(self, nome: str):
        self.__nome = nome

pessoa1 = Pessoa("Lukas", 31, "Gomes")
# pessoa1.__nome = "lukas "
# pessoa1.__sobrenome = "gomes"
# pessoa1.__idade = 31
pessoa1.set_nome(123)
print(pessoa1.get_nome())




# Quando um atributo for privado, ele nao pode ser acessado.


# adicionar idade e definir regra para nao aceitar idade negativa
