def melhores_alunos(alunos):
    """
    Identifica alunos com média superior ou igual à média da turma
    
    Args:
        alunos: Lista de dicionários com 'nome' e 'nota' de cada aluno
    
    Returns:
        Lista com nomes dos alunos premiados (média >= média da turma)
    """
    if not alunos:
        return []
    
    # Calcula a média da turma
    soma_notas = sum(aluno['nota'] for aluno in alunos)
    media_turma = soma_notas / len(alunos)
    
    # Identifica alunos com média > média da turma
    melhores_alunos = []
    for aluno in alunos:
        if aluno['nota'] > media_turma:
            melhores_alunos.append(aluno['nome'])
    
    return melhores_alunos

# Testes com os exemplos fornecidos
print("Teste 1:")
entrada1 = [{"nome": "Joao", "nota": 7}, {"nome": "Maria", "nota": 5}]
print(f"Entrada: {entrada1}")
print(f"Saída: {melhores_alunos(entrada1)}")
print(f"Média da turma: {(7 + 5) / 2}")

print("\nTeste 2:")
entrada2 = [{"nome": "Joao", "nota": 7}, {"nome": "Maria", "nota": 5}, {"nome": "José", "nota": 5}, {"nome": "Ricardo", "nota": 9}]
print(f"Entrada: {entrada2}")
print(f"Saída: {melhores_alunos(entrada2)}")
print(f"Média da turma: {(7 + 5 + 5 + 9) / 4}")

print("\nTeste 3:")
entrada3 = [{"nome": "Joao", "nota": 7}, {"nome": "José", "nota": 9}, {"nome": "Ricardo", "nota": 9}, {"nome": "Jonas", "nota": 9}]
print(f"Entrada: {entrada3}")
print(f"Saída: {melhores_alunos(entrada3)}")
print(f"Média da turma: {(7 + 9 + 9 + 9) / 4}")
