''' 
Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato. O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem. Após o usuário preencher esses campos, deve haver um botão de envio. Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, indicando que o formulário foi enviado com sucesso.

'''

import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Formulário de Contato"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600
    page.padding = 20

    # Campos do formulário
    nome = ft.TextField(
        label="Nome",
        border=ft.InputBorder.UNDERLINE,
        width=300
    )
    
    email = ft.TextField(
        label="Email",
        border=ft.InputBorder.UNDERLINE,
        width=300
    )
    
    mensagem = ft.TextField(
        label="Mensagem",
        multiline=True,
        min_lines=3,
        max_lines=5,
        border=ft.InputBorder.UNDERLINE,
        width=300
    )

    # Mensagem de sucesso (inicialmente invisível)
    mensagem_sucesso = ft.Text(
        "Formulário enviado com sucesso!",
        color=ft.colors.GREEN,
        size=16,
        visible=False
    )

    def validar_campos():
        if not nome.value or not email.value or not mensagem.value:
            return False
        return True

    def enviar_formulario(e):
        if not validar_campos():
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Por favor, preencha todos os campos!"),
                    bgcolor=ft.colors.RED_400
                )
            )
            return

        # Limpar campos
        nome.value = ""
        email.value = ""
        mensagem.value = ""
        
        # Mostrar mensagem de sucesso
        mensagem_sucesso.visible = True
        page.update()

        # Esconder mensagem após 3 segundos
        page.after(3000, lambda _: setattr(mensagem_sucesso, 'visible', False))
        page.update()

    # Botão de envio
    botao_enviar = ft.ElevatedButton(
        "Enviar",
        on_click=enviar_formulario,
        width=300,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE
    )

    # Container principal
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Formulário de Contato", size=24, weight=ft.FontWeight.BOLD),
                nome,
                email,
                mensagem,
                botao_enviar,
                mensagem_sucesso
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.WHITE,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.BLUE_GREY_100,
        )
    )

    page.add(container)

if __name__ == "__main__":
    ft.app(target=main)