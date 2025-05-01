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
                            ft.Container(
                                bgcolor="#0505FF",
                                height=100,
                                padding=ft.padding.only(left=10, right=10),
                                content=ft.Row(
                                    controls=[
                                        ft.Image(
                                            src="img/socimol.png", width=120, height=70
                                        ),
                                        ft.Text(
                                            "PAINEL DE CARREGAMENTO",
                                            color="white",
                                            size=30,
                                            weight="BOLD",
                                        ),
                                        ft.Image(
                                            src="img/socimol.png", width=120, height=70
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ),
                            ft.Container(
                                bgcolor="#FF0000",
                                height=20,
                                padding=ft.padding.only(left=10, right=10),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "SEQ",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "CLT",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "MOTORISTA",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "DESTINO",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "CONFERENTE",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "PLACA",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "CUB",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "STATUS",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                        ft.Text(
                                            "IMG",
                                            color="white",
                                            size=10,
                                            weight="BOLD",
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    expand=1,
                    bgcolor="blue",
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [
                            ft.Container(
                                bgcolor="red",
                                height=100,
                            )
                        ]
                    ),
                ),
            ],
        ),
    )

    page.add(container)


ft.app(target=main)
