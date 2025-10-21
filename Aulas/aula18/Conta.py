class  ContaBancaria:
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



class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, conta, agencia, limite):
        super().__init__(titular, saldo, conta, agencia)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def exibir_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print(f"Conta: {self.conta}")
        print(f"Agencia: {self.agencia}")
        print(f"Limite: {self.limite}")

conta1 = ContaCorrente("Lukas", 10000, 12345, 4567, 50000)
conta1.exibir_dados()
conta1.sacar(500)
conta1.depositar(500)
conta1.exibir_dados()