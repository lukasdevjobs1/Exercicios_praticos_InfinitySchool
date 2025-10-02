import flet as ft

def main(page: ft.Page):
    page.title = 'Calculadora Simples'
    page.theme_mode = ft.ThemeMode.LIGHT

    def clicou(event):
        try:
            num1 = float(txt_num1.value)
            num2 = float(txt_num2.value)
            resultado = num1 + num2
            resultado_texto = ft.Text(
                value=f"O resultado da soma é: {resultado}",
                size=30,
                color=ft.Colors.GREEN
            )
        except ValueError:
            resultado_texto = ft.Text(
                value="Por favor, insira números válidos.",
                size=30,
                color=ft.Colors.RED
            )
        page.add(resultado_texto)
        page.update()

    texto_inicial = ft.Text(
        value="Calculadora Simples",
        size=35,
        color=ft.Colors.BLACK
    )
    txt_num1 = ft.TextField(
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,        
        hint_text="Digite o primeiro número",
        width=300,
        height=50,
    )
    txt_num2 = ft.TextField(
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,        
        hint_text="Digite o segundo número",
        width=300,
        height=50,      
    )

    botao = ft.ElevatedButton(
        text="Calcular Soma",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        height=40,
        width=150,
        on_click=clicou
    )

    page.add(texto_inicial,botao, txt_num1, txt_num2)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)