import flet as ft



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
                    bgcolor="white",
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        expand=True,
                        spacing=0,
                        controls=[
                            ft.Container(
                                margin=0,
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
                                expand=True,
                                alignment=ft.alignment.top_center,
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.START,
                                    expand=True,
                                    controls=[

                                        ft.DataTable(
                                            expand=True,
                                            heading_row_height=30,
                                            column_spacing=20,
                                            heading_row_color="#FF0000",
                                            data_row_color="#D9E6FE",
                                            #column_spacing=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            columns=[
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("SEQ", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("CLT", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("MOTORISTA", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("DESTINO", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("CONFERENTE", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("PLACA", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("CUB", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("STATUS", size=11, color="white"))),
                                                ft.DataColumn(ft.Container(expand=True,content=ft.Text("IMG", size=11, color="white"))),
                                            ],
                                            rows=[
                                                ft.DataRow(
                                                    [
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "1",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "T",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "JOAQUIM MAIA PEREIRA",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "PARAIBA/RIO G DO NORTE/PERNAMBUCO",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "ARIMATÉIA",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "KBI-6155",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "CUB",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Container(
                                                                bgcolor="green",
                                                                padding=5,
                                                                border_radius=20,
                                                                content=ft.Text(
                                                                    "CARREGANDO",
                                                                    size=11,
                                                                    weight="BOLD",
                                                                ),
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Image(
                                                                "img/img_fabio.png",
                                                                border_radius=50,
                                                                width=45,
                                                                height=45
                                                            )
                                                        ),
                                                    ],
                                                ),
                                                ft.DataRow(
                                                    [
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "1",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "T",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "JOAQUIM MAIA PEREIRA",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "PARAIBA/RIO G DO NORTE",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "ARIMATÉIA",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "KBI-6155",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Text(
                                                                "CUB",
                                                                size=11,
                                                                weight="BOLD",
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Container(
                                                                bgcolor="green",
                                                                padding=5,
                                                                border_radius=20,
                                                                content=ft.Text(
                                                                    "CARREGANDO",
                                                                    size=11,
                                                                    weight="BOLD",
                                                                ),
                                                            )
                                                        ),
                                                        ft.DataCell(
                                                            ft.Image(
                                                                "img/img_fabio.png",
                                                                border_radius=50,
                                                                width=45,
                                                                height=45
                                                            )
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ],
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
                                height=80,
                                content=ft.Row(
                                    [
                                        ft.Container(
                                            bgcolor="white", width=100, height=60,border_radius=10
                                        ),
                                        ft.Container(
                                            bgcolor="white", width=100, height=60,border_radius=10
                                        ),
                                        ft.Container(
                                            bgcolor="white", width=100, height=60,border_radius=10
                                        ),
                                        ft.Container(
                                            bgcolor="white", width=100, height=60,border_radius=10
                                        ),
                                    ],alignment=ft.MainAxisAlignment.SPACE_AROUND
                                    
                                ),
                            ),
                            ft.Container(expand=True, bgcolor="#D9E6FE"),
                            ft.Container(expand=True, bgcolor="white"),
                            ft.Container(expand=True, bgcolor="#D9E6FE"),
                        ],
                        spacing=0,
                    ),
                ),
            ],
        ),
    )

    page.add(container)


ft.app(target=main)
