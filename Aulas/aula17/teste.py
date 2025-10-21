def calcula_preco_final(preco_unitario, quantidade):
	### Seu código aqui.
	preco_total = preco_unitario * quantidade

	if quantidade >= 1 and quantidade <= 5:
		desconto = 0
	elif quantidade >= 6 and quantidade <= 10:
		desconto = 0.05
	elif quantidade >= 11 and quantidade <= 20:
		desconto = 0.10
	elif quantidade > 20:
		desconto = 0.15
	else:
		desconto = 0

	valor_desconto = preco_total * desconto
	preco_final = preco_total - valor_desconto
	return round(preco_final, 2)

print("Exemplo 1:")
print(f"Entrada: {{'preco_unitario': 30.0, 'quantidade': 15}}")
print(f"Saída: {calcula_preco_final(30.0, 15)}")

print("\nExemplo 2:")
print(f"Entrada: {{'preco_unitario': 20.5, 'quantidade': 8}}")
print(f"Saída: {calcula_preco_final(20.5, 8)}")