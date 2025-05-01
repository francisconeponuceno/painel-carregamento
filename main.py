import flet as ft
from flet import WEB_BROWSER


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Painel"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    container = ft.Container(
        bgcolor="WHITE",
        expand=True,
        alignment=ft.alignment.top_center,
        content=ft.Row(
            spacing=0,
            controls=[
                ft.Container(
                    expand=2,
                    bgcolor="green",
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [
                            ft.Container(bgcolor="red", height=100),
                            ft.Row(
                                [
                                    ft.Container(content=ft.Text("SEQ")),
                                    ft.Container(content=ft.Text("SEQ")),
                                    ft.Container(content=ft.Text("SEQ")),
                                    ft.Container(content=ft.Text("SEQ")),
                                    ft.Container(content=ft.Text("SEQ")),
                                    ft.Container(content=ft.Text("SEQ")),
                                    ft.Container(content=ft.Text("SEQ")),
                                    ft.Container(content=ft.Text("SEQ")),
                                ],
                                expand=True,
                                spacing=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    expand=1,
                    bgcolor="blue",
                    alignment=ft.alignment.center,
                    content=ft.Column([ft.Container(bgcolor="red", height=100)]),
                ),
            ],
        ),
    )

    page.add(container)


ft.app(target=main)
