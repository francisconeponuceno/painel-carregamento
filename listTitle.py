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

    # CRIAÇÃO DOS INPUTS DOS CARREGOS
    CLT = ft.TextField(label='clt',text_align='center',text_size=10,width=30,content_padding=0,ref=input_clt)
    MOT = ft.TextField(label='mot',text_align='center',text_size=10,width=200,content_padding=0,ref=input_mot)
    DEST = ft.TextField(label='dest',text_align='center',text_size=10,width=200,content_padding=0,ref=input_dest)
    CONF = ft.TextField(label='conf',text_align='center',text_size=10,width=100,content_padding=0,ref=input_conf)
    PLACA = ft.TextField(label='placa',text_align='center',text_size=10,width=60,content_padding=0,ref=input_placa)
    CUB = ft.TextField(label='cub',text_align='center',text_size=10,width=40,content_padding=0,ref=input_cub)

    def foto_conferente():
        if input_conf.current.value == "ARIMATEIA":
            return 'assets/arimateia.jpg'
        if input_conf.current.value == "VICENTE":
            return 'assets/vicente.png'
        if input_conf.current.value == "ZE CARLOS":
            return 'assets/zecarlos.png'
        if input_conf.current.value == "CASSIO":
            return 'assets/cassio.png'
        if input_conf.current.value == "RAIONE":
            return 'assets/raione.png'
        if input_conf.current.value == "FERNANDO":
            return 'assets/fernando.png'
        if input_conf.current.value == "LUCAS":
            return 'assets/lucas.png'
        if input_conf.current.value == "FABIO":
            return 'assets/fabio.png'
        if input_conf.current.value == "CASE":
            return 'assets/caze.jpg'
        else: 
            return 'assets/padrao.jpg'
        

    def cadastrar(e):
        try:
            if input_mot.current.value == '' or input_dest.current.value == '' or input_placa.current.value == '':
                return
            img_conf = foto_conferente()
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
    cor_linha = ft.Ref[ft.Container]()
    dados = consultarDados() # VARIÁVEL QUE RECEBE OS DADOS DO BANCO, ATRAVÉS DA FUNÇÃO consultaDdados()

    # CRIAÇÃO DA TABELA DE CARREGO
    tabela = ft.ListView(
        expand=True,
        padding=10,
        auto_scroll=True,
    )
    
    # AQUI COMERÇA A CRIAÇAO DAS LINHAS DA TABELA
    cor1 = '#D9E6FE'
    cor2 = '#b3d3f8'
    
    for i in dados:
        cor_fundo = cor1 if i[0] % 2 == 0 else cor2
        tabela.controls.append(
            ft.Container(
                content=ft.Text(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]}",size=11,weight='BOLD'),
                bgcolor=cor_fundo,
                padding=15,
                ref=cor_linha  
            )
        )

            
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
                                content=tabela
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

