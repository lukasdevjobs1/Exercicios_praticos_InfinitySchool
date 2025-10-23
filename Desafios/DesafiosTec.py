#### BUSCA BINária 1ª QUESTÃO ####

def solution(piles, h):
    # Define os limites da busca binária
    left = 1  # mínimo possível por hora
    right = max(piles)  # máximo possível por hora
    
    def can_eat_all(speed):
        # Calcula quanto tempo leva para comer todo o bambu com essa velocidade
        hours_needed = 0
        for pile in piles:
            # Para cada pilha, calculamos quantas horas são necessárias
            # Usamos math.ceil para arredondar para cima
            hours_needed += (pile + speed - 1) // speed
        return hours_needed <= h
    
    # Busca binária
    result = right  # caso base
    while left <= right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            result = mid  # possível candidato
            right = mid - 1  # tenta encontrar um valor menor
        else:
            left = mid + 1  # precisa comer mais rápido
    
    return result

#### MAIORITÁRIO 2ª QUESTÃO ####
def solution(nums):
    
    contador = {}
    
    
    for num in nums:
        contador[num] = contador.get(num, 0) + 1
    
  
    n = len(nums)
    for num, freq in contador.items():
        if freq > n//2:
            return num
    
    return None  


### # MAIORITÁRIO - BOYER-MOORE 3ª QUESTÃO ####
def solution(nums):
    # Implementação do algoritmo Boyer-Moore
    candidato = None
    contador = 0
    
    # Primeira passagem: encontra o candidato
    for num in nums:
        if contador == 0:
            candidato = num
        contador += 1 if num == candidato else -1
    
    # Segunda passagem: verifica se é realmente majoritário
    contador = sum(1 for num in nums if num == candidato)
    
   
    return candidato if contador > len(nums) // 2 else None


####  TABELA DE PEDIDOS 4ª QUESTÃO ####

def solution(orders):
    # 1. Primeiro, coletamos todos os itens únicos de comida
    food_items = set()
    table_orders = {}
    
    # 2. Processamos cada pedido do array de entrada
    for order in orders:
        customer_name, table_number, food_item = order
        food_items.add(food_item)
        
        # Inicializamos o dicionário para cada mesa
        if table_number not in table_orders:
            table_orders[table_number] = {}
        
        # Contamos os itens por mesa
        if food_item not in table_orders[table_number]:
            table_orders[table_number][food_item] = 0
        table_orders[table_number][food_item] += 1
    
    # 3. Ordenamos os itens de comida alfabeticamente
    sorted_food_items = sorted(list(food_items))
    
    # 4. Criamos o cabeçalho da tabela
    header = ["Table"] + sorted_food_items
    result = [header]
    
    # 5. Ordenamos as mesas numericamente
    sorted_tables = sorted(table_orders.keys(), key=int)
    
    # 6. Montamos as linhas da tabela
    for table in sorted_tables:
        row = [table]
        for food_item in sorted_food_items:
            count = table_orders[table].get(food_item, 0)
            row.append(str(count))
        result.append(row)
    
    return result



### LUCRO MÁXIMO 5ª QUESTÃO ####


def lucro_maximo(prices):
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    
    for i in range(2, len(prices)):
        current_price = prices[i]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit + (prices[i-1] - min_price))
        min_price = min(min_price, current_price)
    
    return max_profit



###  CONTAR DÍGITOS 1 6ª QUESTÃO ####

def contar_digitos_1(n):
    count = 0
    for i in range(n + 1):
        count += str(i).count('1')
    return count
