lista = [1, "Josias", 9.5, True]

print(len(lista))

lista.append("Noite")
print(lista)

minha_lista = ["Manhã", "Tarde"]
lista.extend(minha_lista)
print(lista)

lista.insert(0, "Matematica")
print(lista)

lista.remove("Manhã")
lista.pop(0)

print(lista)

lista_nova = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_nova.reverse()
print(lista_nova) # Ordem decrescente 

lista_nova.sort()
print(lista_nova) # Ordem crescente 