import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.window_width = 400
    page.window_height = 500
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campo de entrada de texto
    task_input = ft.TextField(
        label="Nova tarefa",
        hint_text="Digite o nome da tarefa...",
        expand=True
    )

    # Lista que exibirá as tarefas
    task_list = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)

    # Função chamada ao clicar no botão "Adicionar"
    def add_task(e):
        task_name = task_input.value.strip()
        if task_name:
            # Adiciona a nova tarefa na lista
            task_list.controls.append(ft.Text(f"• {task_name}", size=16))
            task_input.value = ""  # limpa o campo
            page.update()

    # Botão de adicionar
    add_button = ft.ElevatedButton("Adicionar", on_click=add_task, icon=ft.icons.ADD)

    # Layout da interface
    page.add(
        ft.Column(
            [
                ft.Text("📝 Lista de Tarefas", size=22, weight="bold"),
                ft.Row([task_input, add_button]),
                ft.Divider(),
                task_list,
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.START,
        )
    )

# Executa a aplicação
ft.app(target=main)
