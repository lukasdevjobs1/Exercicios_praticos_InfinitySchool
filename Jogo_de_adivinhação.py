import random

# Jogo de Adivinhação - Programa em Python
# O jogador deve adivinhar um número fixo em até 3 tentativas

# Definindo o número secreto que o jogador deve adivinhar
numero_secreto = random.randint(1, 10)

# Definindo o número máximo de tentativas permitidas
max_tentativas = 3

# Contador para controlar quantas tentativas o jogador já fez
tentativas = 0

# Mensagem de boas-vindas ao jogo
print("🎮 Bem-vindo ao Jogo de Adivinhação! 🎮")
print(f"Você tem {max_tentativas} tentativas para adivinhar um número entre 1 e 10!")
print("Boa sorte! 🍀\n")

# Loop principal do jogo usando while
# Continua enquanto o jogador não atingir o limite de tentativas
while tentativas < max_tentativas:
    # Incrementa o contador de tentativas
    tentativas += 1
    
    # Mostra qual tentativa é esta
    print(f"Tentativa {tentativas}/{max_tentativas}")
    
    # Solicita ao jogador que digite um número
    # Utilizamos try/except para tratar possíveis erros de entrada
    try:
        # Recebe a entrada do usuário e converte para inteiro
        palpite = int(input("Digite seu palpite: "))
        
        # Verifica se o palpite está correto
        if palpite == numero_secreto:
            # Se acertou, quebra o loop imediatamente
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto}!")
            print(f"Você conseguiu em {tentativas} tentativa(s)! 🏆")
            break
        
        # Se não acertou, dá uma dica se o número é maior ou menor
        elif palpite < numero_secreto:
            print("📈 O número secreto é MAIOR que seu palpite!")
        else:
            print("📉 O número secreto é MENOR que seu palpite!")
        
        # Se não é a última tentativa, mostra quantas restam
        if tentativas < max_tentativas:
            tentativas_restantes = max_tentativas - tentativas
            print(f"Você ainda tem {tentativas_restantes} tentativa(s)!\n")
        
    except ValueError:
        # Tratamento de erro caso o usuário digite algo que não seja um número
        print("❌ Por favor, digite apenas números inteiros!")
        # Decrementa o contador pois esta tentativa não conta
        tentativas -= 1

# Estrutura else do while - executa apenas se o loop terminou normalmente
# (ou seja, se o jogador não acertou e esgotou todas as tentativas)
else:
    # Mensagem de consolo quando o jogador não consegue acertar
    print(f"\n😔 Que pena! Suas tentativas acabaram.")
    print(f"O número secreto era {numero_secreto}.")
    print("Não desista! Tente novamente da próxima vez! 💪")

# Mensagem final do jogo
print("\n🎮 Obrigado por jogar! Até a próxima! 👋")