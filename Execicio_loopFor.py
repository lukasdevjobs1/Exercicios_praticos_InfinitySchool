# Exercicio de loop for para calcular media de notas dos alunos:


class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def aprovado(self):
        return self.notas >= 6
    
# aqui vamos criar a lista de alunos para armazenar os dados:

alunos = []

# aqui vamos criar o loop para receber os dados dos alunos:

for i in range(2):
    nome = input(f"Digite o nome do aluno: ")
    notas = float(input(f"Digite a nota do aluno {nome}: "))
    aluno = Aluno(nome, notas)
    alunos.append(aluno)

# aqui vamos calcular a media das notas dos alunos:

media = sum(aluno.notas for aluno in alunos) / len(alunos)

# aqui vamos exibir a media dos alunos:

for aluno in alunos:
    if Aluno.aprovado(self=aluno):
        print(f"O aluno {aluno.nome} foi aprovado com a nota {aluno.notas}")
    else:
        print(f"O aluno {aluno.nome} foi reprovado com a nota {aluno.notas}")