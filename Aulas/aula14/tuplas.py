def exibir_tupla(tupla):
    """
    Exibe os elementos de uma tupla.

    Args:
        tupla (tuple): A tupla a ser exibida.
    """
    for elemento in tupla:
        print(elemento)

meios_pagamentos = ("Dinheiro", "Cartão", "Boleto")
print(meios_pagamentos)

def adicionar_meio_pagamento(tupla, meio_pagamento):
    """
    Adiciona um novo meio de pagamento à tupla.

    Args:
        tupla (tuple): A tupla original.
        meio_pagamento (str): O novo meio de pagamento.

    Returns:
        tuple: A tupla atualizada.
    """
    nova_tupla = tupla + (meio_pagamento,)
    return nova_tupla

meios_pagamentos = adicionar_meio_pagamento(meios_pagamentos, "Pix")
print(meios_pagamentos)