class Tamagotchi:
    def __init__(self, nome: str):
        self.nome = nome
        self.idade = 0.0
        self.fome = 50
        self.felicidade = 50
        self.vivo = True
    
    def _aplicar_limites(self):
        """Garante que fome e felicidade fiquem entre 0 e 100"""
        self.fome = max(0, min(100, self.fome))
        self.felicidade = max(0, min(100, self.felicidade))
    
    def _checar_morte(self):
        """Verifica se o Tamagotchi morreu e atualiza o estado"""
        if self.fome >= 100 or self.felicidade <= 0:
            self.vivo = False
    
    def alimentar(self, qtd: int):
        """Alimenta o Tamagotchi, reduzindo a fome"""
        if not self.vivo:
            print(f"{self.nome} está morto e não pode ser alimentado.")
            return
        
        if qtd <= 0:
            print("Quantidade deve ser maior que 0.")
            return
        
        # Cada unidade de comida reduz 2 pontos de fome
        self.fome -= qtd * 2
        self._aplicar_limites()
        self._checar_morte()
    
    def brincar(self, minutos: int):
        """Brinca com o Tamagotchi, aumentando felicidade e fome"""
        if not self.vivo:
            print(f"{self.nome} está morto e não pode brincar.")
            return
        
        if minutos <= 0:
            print("Minutos devem ser maiores que 0.")
            return
        
        # Cada minuto aumenta 1 ponto de felicidade e 0.5 ponto de fome
        self.felicidade += minutos
        self.fome += minutos * 0.5
        self._aplicar_limites()
        self._checar_morte()
    
    def passar_tempo(self, horas: float):
        """Simula a passagem do tempo"""
        if not self.vivo:
            print(f"{self.nome} está morto e o tempo não afeta mais.")
            return
        
        if horas <= 0:
            print("Horas devem ser maiores que 0.")
            return
        
        # A cada hora: idade aumenta, fome aumenta, felicidade diminui
        self.idade += horas
        self.fome += horas * 3  # 3 pontos de fome por hora
        self.felicidade -= horas * 2  # 2 pontos de felicidade perdidos por hora
        self._aplicar_limites()
        self._checar_morte()
    
    def status(self) -> str:
        """Retorna string com todos os atributos atuais"""
        estado = "VIVO" if self.vivo else "MORTO"
        return (f"{self.nome} ({estado}) - "
                f"Idade: {self.idade:.1f} anos, "
                f"Fome: {self.fome:.1f}/100, "
                f"Felicidade: {self.felicidade:.1f}/100")
    
    def esta_morto(self) -> bool:
        """Retorna True se o Tamagotchi estiver morto"""
        return not self.vivo
# Criando um Tamagotchi
pet = Tamagotchi("Tama")

# Verificando status inicial
print(pet.status())
# Tama (VIVO) - Idade: 0.0 anos, Fome: 50.0/100, Felicidade: 50.0/100

# Ações
pet.alimentar(10)  # Alimenta com 10 unidades
pet.brincar(15)    # Brinca por 15 minutos
pet.passar_tempo(2) # Passam 2 horas

print(pet.status())
# Tama (VIVO) - Idade: 2.0 anos, Fome: 45.0/100, Felicidade: 75.0/100

# Tentando ações com valores inválidos
pet.alimentar(-5)  # Quantidade deve ser maior que 0.
pet.brincar(0)     # Minutos devem ser maiores que 0.

# Testando morte por fome
pet.passar_tempo(20)  # Fome vai aumentar muito
print(pet.esta_morto())  # True
print(pet.status())      # Tama (MORTO) - ...

# Tentando agir com Tamagotchi morto
pet.alimentar(10)  # Tama está morto e não pode ser alimentado.