import flet as ft


def main(page: ft.Page):
    text = ft.Text(value="Infinity School", color="#DC2831", size=37, italic=True, weight="bold", text_align="center", width=400, height=100)
    
    page.theme = ft.Theme(
        color_scheme_seed="#E24125",
        use_material3=True
    )

    page.add(text)
    page.update()

ft.app(target=main)