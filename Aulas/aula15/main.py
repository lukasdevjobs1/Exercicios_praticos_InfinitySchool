import flet as ft 


def main(page: ft.Page):
    page.title = "Hello World"
    # page.theme = "dark"

    
    def clicou(event):
        texto_digitado = txt_nome.value
        novo_texto = ft.Text(
            value=f"Olá {texto_digitado}. Seja bem vindo!",
            size=35,
            color=ft.Colors.WHITE
             
        )
        page.add(novo_texto)
        page.update()
    
    texto_inicial = ft.Text(
        value="Hello World",
        size=35,
        color=ft.Colors.WHITE10
        )
    txt_nome = ft.TextField(
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        hint_text="Digite seu nome",

    )
    botao = ft.ElevatedButton(
        text="Clique aqui",
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        height=30,
        width=130,
        on_click=clicou
        
    )

    linha = ft.Row(
        controls=[
            ft.ElevatedButton("Botão 1 - Row"),
            ft.ElevatedButton("Botão 2 - Row")
        ]

    )

    
    page.add(texto_inicial, txt_nome, botao, linha)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)