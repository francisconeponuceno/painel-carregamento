import flet as ft
from database import *


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Painel"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0

    dados = consultarDados()
    tabela = ft.DataTable(
        expand=True,
        heading_row_height=30,
        column_spacing=20,
        heading_row_color="#FF0000",
        data_row_color="#D9E6FE",
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
    
        rows=[]    
    )
    for i in dados:
        
        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
                ft.DataCell(ft.Text(f"1")),
            ]
        )
        print(i)
        tabela.rows.append(row)

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
                                height=80,
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
                                        tabela
                                        
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    expand=1,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [
                            ft.Container(
                                margin=ft.margin.only(left=10, right=10),
                                height=80,
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            bgcolor="white",height=60,border_radius=10,expand=True
                                        ),
                                        ft.Container(
                                            bgcolor="white",height=60,border_radius=10,expand=True
                                        ),
                                        ft.Container(
                                            bgcolor="white",height=60,border_radius=10,expand=True
                                        ),
                                        ft.Container(
                                            bgcolor="white",height=60,border_radius=10,expand=True
                                        ),
                                    ],     
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

if __name__ == "__main__":
    ft.app(target=main)
