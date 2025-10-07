import flet as ft

# Atividade 1 e 2

# def main(page: ft.Page):
#     page.title = "Atividade 1 Flet"
#     page.text = "Estilização avançada com Flet"

#     def clicou(event):
#         # Implemente a lógica do clique aqui

#     # Botão 1
#         botao_1 = ft.ElevatedButton(
#             text="Botão 1",
#             on_click=clicou,
#             bgcolor=ft.Colors.BLUE_50,
#             color=ft.Colors.WHITE,
        
#     )
#         page.add(botao_1)

#     # Botão 2
#     botao_2 = ft.ElevatedButton(
#         text="Botão 2",
#         on_click=clicou,
#         bgcolor=ft.Colors.GREEN_50,
#         color=ft.Colors.WHITE,
      
#     )
#     page.add(botao_2)

#     # Botão 3
#     botao_3 = ft.ElevatedButton(
#         text="Botão 3",
#         on_click=clicou,
#         bgcolor=ft.Colors.RED_50,
#         color=ft.Colors.WHITE,
        
#     )
#     page.add(botao_3)

#     page.update()

# ft.app(target=main)



# Atividade 3º

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.text = "Por favor, preencha o formulário abaixo."

    def enviar_formulario(event):
        nome = nome_input.value
        email = email_input.value
        # Implemente a lógica de envio do formulário aqui
        print(f"Nome: {nome}, Email: {email}")

    # Campo de entrada para nome
    nome_input = ft.TextField(
        label="Nome",
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        width=300,
        height=50
    )
    page.add(nome_input)

    # Campo de entrada para email
    email_input = ft.TextField(
        label="Email",
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        width=300,
        height=50
    )
    page.add(email_input)

    # Botão de envio
    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        bgcolor=ft.Colors.GREEN_50,
        color=ft.Colors.WHITE,
        on_click=enviar_formulario
    )
    page.add(botao_enviar)

    page.update()

ft.app(target=main)