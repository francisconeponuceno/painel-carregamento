# IMPORTAÇÕES
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

    # VARIÁVEIS
    dados = consultarDados() # VARIÁVEL QUE RECEBE OS DADOS DO BANCO, ATRAVÉS DA FUNÇÃO consultaDdados()
    status = ft.Ref[ft.Container]() # VARIÁVEL DO STATUS DO CARREGO
    status_text = ft.Ref[ft.Text]() # VARIÁVEL DO TEXTO DO STATUS CARREGO
    input_clt = ft.Ref[ft.TextField]() # VARIÁVEL INPUT CLT
    input_mot = ft.Ref[ft.TextField]() # VARIÁVEL INPUT MOTORISTA
    input_dest = ft.Ref[ft.TextField]() # VARIÁVEL INPUT DESTINO
    input_conf = ft.Ref[ft.TextField]() # VARIÁVEL INPUT CONFERENTE
    input_placa = ft.Ref[ft.TextField]() # VARIÁVEL INPUT PLACA
    input_cub = ft.Ref[ft.TextField]() # VARIÁVEL INPUT CUBAGEM
    container_tabela = ft.Ref[ft.Container]() # VARIAVEL DO CONTAINER DA TABELA

    # CRIAÇÃO DOS INPUTS DOS CARREGOS
    CLT = ft.TextField(label='clt',text_align='center',text_size=10,width=30,content_padding=0,ref=input_clt)
    MOT = ft.TextField(label='mot',text_align='center',text_size=10,width=200,content_padding=0,ref=input_mot)
    DEST = ft.TextField(label='dest',text_align='center',text_size=10,width=200,content_padding=0,ref=input_dest)
    CONF = ft.TextField(label='conf',text_align='center',text_size=10,width=100,content_padding=0,ref=input_conf)
    PLACA = ft.TextField(label='placa',text_align='center',text_size=10,width=60,content_padding=0,ref=input_placa)
    CUB = ft.TextField(label='cub',text_align='center',text_size=10,width=40,content_padding=0,ref=input_cub)

    def foto_conferente():
        match input_conf.current.value:
            case 'ARIMATEIA':
                return 'assets/arimateia.jpg'
            case "VICENTE":
                return 'assets/vicente.png'
            case "ZE CARLOS":
                return 'assets/zecarlos.png'
            case "CASSIO":
                return 'assets/cassio.png'
            case "RAIONE":
                return 'assets/raione.png'
            case "FERNANDO":
                return 'assets/fernando.png'
            case "LUCAS":
                return 'assets/lucas.png'
            case "FABIO":
                return 'assets/fabio.png'
            case "CASE":
                return 'assets/caze.jpg'
            case _: 
                return 'assets/padrao.jpg'
        
    # FUNÇÃO PARA ADICIONAR UM CARREGO
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
            
            container_tabela.current.update()
            page.update()
        except:
            return
        
    # FUNÇÃO PARA DELETAR UM CARREGO
    
    def delet_carrego(e):
        try:
            soma = 0
            for car in dados:
                soma += 1
                if soma == int(input_cub.current.value):
                    excluir(car[0])
                    page.update()
        except: print('ERRO AO DELETAR O CARREGO')
    
    ADD = ft.Container(content=ft.Text('+',text_align='center',size=15),bgcolor='blue',width=30,height=25,border_radius=40,on_click=cadastrar)
    DEL = ft.Container(content=ft.Text('-',text_align='center',size=15),bgcolor='red',width=30,height=25,border_radius=40,on_click=delet_carrego)


    # CRIAÇÃO DA TABELA DE CARREGO
    tabela = ft.ListView(
        expand=True,
        auto_scroll=False
    )
    # CABEÇALHO DA TABELA
    tabela.controls.append(
        ft.Container(
            bgcolor='#FF0000',
            padding=5,
            content=ft.Row([
                ft.Container(width=20,content=ft.Text(f"ID",size=11,weight='BOLD',color='white')),
                ft.Container(width=30,content=ft.Text(f"CLT",size=11,weight='BOLD',color='white')),
                ft.Container(expand=True,width=150,content=ft.Text(f"MOTORISTA",size=11,weight='BOLD',color='white')),
                ft.Container(expand=True,width=150,content=ft.Text(f"DESTINO",size=11,weight='BOLD',color='white')),
                ft.Container(width=100,content=ft.Text(f"CONFERENTE",size=11,weight='BOLD',color='white')),
                ft.Container(width=80,content=ft.Text(f"PLACA",size=11,weight='BOLD',color='white')),
                ft.Container(width=30,content=ft.Text(f"CUB",size=11,weight='BOLD',color='white')),
                ft.Container(width=90,content=ft.Text(f"STATUS",size=11,weight='BOLD',color='white')),
                ft.Container(width=45,content=ft.Text(f"IMG",size=11,weight='BOLD',color='white')),
                
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=15
            )    
        )
    )
    # CRIAÇAO DAS LINHAS DA TABELA
    cor1 = '#D9E6FE'
    cor2 = '#f7faff'
    contador = 0
    for i in dados:
        contador += 1
        cor_fundo = cor1 if contador % 2 == 0 else cor2
        tabela.controls.append(
            ft.Container(
                expand=True,
                height=50,
                bgcolor=cor_fundo,
                padding=ft.padding.only(left=10, right=10),
                margin=0,
                content=ft.Row(
                    [
                        ft.Container(width=20,content=ft.Text(f"{contador}",size=11,weight='BOLD',text_align='left')),
                        ft.Container(width=30,content=ft.Text(f"{i[1]}",size=11,weight='BOLD')),
                        ft.Container(expand=True,width=150,content=ft.Text(f"{i[2]}",size=11,weight='BOLD')),
                        ft.Container(expand=True,width=150,content=ft.Text(f"{i[3]}",size=11,weight='BOLD')),
                        ft.Container(width=100,content=ft.Text(f"{i[4]}",size=11,weight='BOLD',text_align='center')),
                        ft.Container(width=80,content=ft.Text(f"{i[5]}",size=11,weight='BOLD')),
                        ft.Container(width=30,content=ft.Text(f"{i[6]}",size=11,weight='BOLD')),
                        ft.Container(
                            ref=status,
                            bgcolor="#96dbfc",
                            padding=5,
                            border_radius=20,
                            width=90,
                            content=ft.Container(
                                ft.Text(
                                    f"{i[7]}",
                                    size=11,
                                    weight="BOLD",
                                    text_align="center",
                                    color="#0505FF",
                                    ref=status_text
                                )
                            )
                        ),

                        ft.Container(
                            height=48,
                            width=48,
                            border_radius=50, 
                            content=ft.Image(
                                src=f"{i[8]}",
                                fit=ft.ImageFit.COVER,
                           ),
                           
                        )
                       
                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )    
            )
        )

        # VERIFICAÇÃO DAS FASES DO CARREGO
        match i[7]:
            case 'CONCLUIDO':
                status.current.bgcolor = "#7ebb7e"
                status_text.current.color = '#022902'
            case 'CANCELADO':
                status.current.bgcolor = '#f99292'
                status_text.current.color = '#690303'
            case 'ADIADO':
                status.current.bgcolor = '#fb7929'
                status_text.current.color = '#672802'    
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
                                        CLT, MOT, DEST, CONF, PLACA, CUB, ADD, DEL
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                ),
                            ),
                            ft.Container(
                                expand=True,
                                alignment=ft.alignment.top_center,
                                content=tabela,
                                ref=container_tabela
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

