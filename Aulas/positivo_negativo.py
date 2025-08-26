def task(numero_positivo, numero_negativo, numero_neutro):
    
    if numero_positivo > 0:
        return "positivo"
    elif numero_negativo < 0:
        return "negativo"
    else:
        return "neutro"
    
numero_positivo = 10
numero_negativo = -10

print(task(numero_positivo,numero_negativo,0))