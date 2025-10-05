# Programa para fazer café

ingredientes = ["cafe", "leite", "acucar", "chocolate", "leite condensado"]

def fazer_cafe(qtd_cafe, ingredientes_escolhidos):
    for i in range(qtd_cafe):
        print(f"\nFazendo café {i+1}:")
        for ingrediente in ingredientes_escolhidos:
            print(f"- Adicionando {ingrediente}")
        print("✓ Café pronto!")

def mostrar_ingredientes():
    print("\nIngredientes disponíveis:")
    for i, ingrediente in enumerate(ingredientes, 1):
        print(f"{i} - {ingrediente}")

while True:
    print("\n" + "="*40)
    print("BEM-VINDO AO PROGRAMA DE FAZER CAFÉ")
    print("="*40)
    
    qtd_cafe = int(input("Quantos cafés deseja fazer? "))
    
    mostrar_ingredientes()
    
    ingredientes_escolhidos = []
    while True:
        try:
            escolha = int(input("\nEscolha um ingrediente (número) ou 0 para finalizar: "))
            if escolha == 0:
                break
            if 1 <= escolha <= len(ingredientes):
                ingredientes_escolhidos.append(ingredientes[escolha-1])
                print(f"✓ {ingredientes[escolha-1]} adicionado!")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite apenas números!")
    
    if ingredientes_escolhidos:
        fazer_cafe(qtd_cafe, ingredientes_escolhidos)
    else:
        print("Nenhum ingrediente selecionado!")
    
    if input("\nFazer outro café? (s/n): ").lower() != 's':
        break

print("\nObrigado por usar o programa!")
