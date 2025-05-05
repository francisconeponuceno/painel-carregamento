import flet as ft
from database import *

# CONFIGURAÇÕES DA PAGINA
def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Painel"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0

    input_clt = ft.Ref[ft.TextField]()
    input_mot = ft.Ref[ft.TextField]()
    input_dest = ft.Ref[ft.TextField]()
    input_conf = ft.Ref[ft.TextField]()
    input_placa = ft.Ref[ft.TextField]()
    input_cub = ft.Ref[ft.TextField]()
    img_conf = 'assets/padrao'

    # CRIAÇÃO DOS INPUTS DOS CARREGOS
    CLT = ft.TextField(label='clt',text_align='center',text_size=10,width=30,content_padding=0,ref=input_clt)
    MOT = ft.TextField(label='mot',text_align='center',text_size=10,width=200,content_padding=0,ref=input_mot)
    DEST = ft.TextField(label='dest',text_align='center',text_size=10,width=200,content_padding=0,ref=input_dest)
    CONF = ft.TextField(label='conf',text_align='center',text_size=10,width=100,content_padding=0,ref=input_conf)
    PLACA = ft.TextField(label='placa',text_align='center',text_size=10,width=60,content_padding=0,ref=input_placa)
    CUB = ft.TextField(label='cub',text_align='center',text_size=10,width=40,content_padding=0,ref=input_cub)
    
    def cadastrar(e):
        try:
            if input_mot.current.value == '' or input_dest.current.value == '' or input_placa.current.value == '':
                return
            salvar(
                input_clt.current.value,
                input_mot.current.value,
                input_dest.current.value,
                input_conf.current.value,
                input_placa.current.value,
                input_cub.current.value,
                'AGUARD',
                img_conf
            )
            page.update()
        except:
            return
    ADD = ft.Container(content=ft.Text('+',text_align='center',size=15),bgcolor='blue',width=30,height=25,border_radius=40,on_click=cadastrar)

    # VARIÁVEIS
    status = ft.Ref[ft.Container]()
    dados = consultarDados() # VARIÁVEL QUE RECEBE OS DADOS DO BANCO, ATRAVÉS DA FUNÇÃO consultaDdados()

    # CRIAÇÃO DA TABELA DE CARREGO
    tabela = ft.DataTable(
        expand=True,
        heading_row_height=30,
        column_spacing=20,
        heading_row_color="#FF0000",
        data_row_color="#D9E6FE",
        
        # CABEÇALHO DA TABELA
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
    # AQUI COMERÇA A CRIAÇAO DAS LINHAS DA TABELA
    for i in dados:
        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{i[0]}", size=11, weight="BOLD")),
                ft.DataCell(ft.Text(f"{i[1]}", size=11, weight="BOLD")),
                ft.DataCell(ft.Text(f"{i[2]}", size=11, weight="BOLD")),
                ft.DataCell(ft.Text(f"{i[3]}", size=11, weight="BOLD")),
                ft.DataCell(ft.Text(f"{i[4]}", size=11, weight="BOLD")),
                ft.DataCell(ft.Text(f"{i[5]}", size=11, weight="BOLD")),
                ft.DataCell(ft.Text(f"{i[6]}", size=11, weight="BOLD")),
                ft.DataCell(
                    ft.Container(
                        ft.Text(
                            f"{i[7]}",
                            size=11,
                            weight="BOLD",
                            text_align="center",
                            color="white",
                        ),
                        ref=status,
                        bgcolor="#0505FF",
                        padding=5,
                        border_radius=20,
                        width=90,
                    )
                ),
                ft.DataCell(
                    ft.Container(
                        ft.Image(src=f"{i[8]}", width=45, height=45, border_radius=50),
                    )
                ),
            ]
        )
        if i[7] == 'CONCLUIDO':
            status.current.bgcolor = "#008000"
        tabela.rows.append(row)
        page.update()

    # CONTAINER PRINCIPAL
    container = ft.Container(
        bgcolor="WHITE",
        expand=True,
        alignment=ft.alignment.top_center,
        content=ft.Row(
            spacing=0,
            controls=[
                ft.Container(
                    expand=2,
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
                                            src="assets/socimol.png", width=120, height=70
                                        ),
                                        ft.Text(
                                            "PAINEL DE CARREGAMENTO",
                                            color="white",
                                            size=30,
                                            weight="BOLD",
                                        ),
                                        ft.Image(
                                            src="assets/socimol.png", width=120, height=70
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ),
                            ft.Container(
                                height=25,
                                margin=ft.margin.all(3),
                                padding=ft.padding.only(left=10, right=10),
                                content=ft.Row(
                                    controls=[
                                        CLT, MOT, DEST, CONF, PLACA, CUB, ADD
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                ),
                            ),
                            ft.Container(
                                expand=True,
                                alignment=ft.alignment.top_center,
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.START,
                                    expand=True,
                                    controls=[tabela],
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
                                            bgcolor="white",
                                            height=60,
                                            border_radius=10,
                                            expand=True,
                                        ),
                                        ft.Container(
                                            bgcolor="white",
                                            height=60,
                                            border_radius=10,
                                            expand=True,
                                        ),
                                        ft.Container(
                                            bgcolor="white",
                                            height=60,
                                            border_radius=10,
                                            expand=True,
                                        ),
                                        ft.Container(
                                            bgcolor="white",
                                            height=60,
                                            border_radius=10,
                                            expand=True,
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
