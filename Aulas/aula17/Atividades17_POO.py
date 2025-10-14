# class Pessoa:
#     # função construtora, inicializadora
#     def __init__(self,nome, idade ):
#         self.nome = nome
#         self.idade = idade
#         print(f"Pessoa {self.nome} criada com sucesso")


# # como criar um objeto?
# p1 = Pessoa("Lukas", 31)
# p1.nome = "Lukas Gomes"
# print(p1.idade, p1.nome)
# p2 = Pessoa("Maria", 25)
# p2.nome = "Maria Joaquina"
# print(p2.idade, p2.nome)


# =====================================================================================================================

# Atividades da aula 17

class ContaBancaria:
    def __init__(self, titular, saldo, conta, agencia):
        self.titular = titular
        self.saldo = saldo
        self.conta = conta
        self.agencia = agencia

    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):

        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


c1 = ContaBancaria("Lukas", 1000, 1234, "1234-5")
print(f"Dados da Conta {c1.titular}:\nAgencia: {c1.agencia}\nConta: {c1.conta}\nSaldo: {c1.saldo}\n")
c1.depositar(500)
print(f"Saldo: {c1.saldo} Apos o deposito")
c1.sacar(1000)
print(f"Saldo: {c1.saldo} Apos o saque")


# class Carro:
#     def __init__(self, modelo, marca, cor):
#         self.modelo = modelo
#         self.marca = marca
#         self.cor = cor
#         self.ligado = False
#         self.velocidade_atual = 0
        
#     def ligar(self):
#         # if self.ligado == False 
#         if not self.ligado:
#             self.ligado = True
#             print(f"O carro: {self.modelo} está ligado")
    
#     def acelerar(self, velocidade):
#         if self.ligado:
#             self.velocidade_atual += velocidade
#             print(f"Acelerando.. Velocidade atual: {self.velocidade_atual}")
#         else:
#             print("O carro precisa está ligado")
            
# carro1 = Carro("uno com escada", "fiat", "prata")
# carro1.acelerar(20) # Não vai acelerar aqui
# print(carro1.ligado) # False
# carro1.ligar()
# carro1.acelerar(35) # Aqui vai dar certo, pois o carro tá ligado
# print(carro1.ligado) # True