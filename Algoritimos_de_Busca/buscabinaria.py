# Lista ordenada para aplicar busca binária
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Inicialização das variáveis de controle
inicio = 0  # Índice do primeiro elemento da lista

meio = len(lista) // 2  # Índice do elemento central

fim = len(lista) - 1  # Índice do último elemento da lista

# Variável para armazenar o índice encontrado
index_procurado = None
# Solicita ao usuário o número a ser procurado
numero_procurado = int(input("digite um numero: "))

# Loop principal da busca binária - continua enquanto há elementos para verificar
while inicio <= fim:
    
    # Calcula o índice do meio do intervalo atual
    meio = (inicio + fim) // 2
    
    # Verifica se o elemento do meio é o número procurado
    if lista[meio] == numero_procurado:
        index_procurado = meio  # Armazena o índice encontrado
        break  # Sai do loop pois encontrou o elemento
    
    # Se o elemento do meio é maior que o procurado, busca na metade esquerda
    elif lista[meio] > numero_procurado:
        fim = meio - 1  # Ajusta o fim para a posição anterior ao meio
    
    # Se o elemento do meio é menor que o procurado, busca na metade direita
    elif lista[meio] < numero_procurado:
        inicio = meio + 1  # Ajusta o início para a posição posterior ao meio
    
# Exibe o resultado final da busca
if index_procurado is not None:
    print(f"Número {numero_procurado} encontrado no índice {index_procurado}")
else:
    print(f"Número {numero_procurado} não encontrado na lista")