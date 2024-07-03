

let Dados = ['','T', 'JOÃO DE DEUS DA LUZ', 'MARANHÃO / PARÁ / TOCANTINS',  'FRANCISCO', 'KBI-6155', '80'];
const listaCompleta = document.querySelector('.principal');
let ListaDeCaregamento = [];
const NoCarregamento = document.querySelector('.TextVasio');

/* VARIÁVEIS DOS ÍCONES*/
let CARRO = "bi bi-truck"
let CONE = "bi bi-cone-striped"
let CHEKOK = "bi bi-check2-circle"
let canc = "bi bi-x-circle-fill"
let circulo = "bi bi-arrow-repeat"
let ClasseFase = ['fase','concluido','adiado','cancelado',]
let ClasseIcone = [CARRO,CONE,CHEKOK,canc,circulo]


/*FUNÇÃO PARA ADICIONAR UM CARREGAMENTO*/
function addCarregamento() {
    if (Dados.length < 7){
        alert('DADOS INCOMPLETO!')
        return
    }
    ListaDeCaregamento.push({
        seq: Dados[0],
        clt: Dados[1],
        mot: Dados[2],
        dest: Dados[3],
        conf: Dados[4],
        placa: Dados[5],
        cub: Dados[6]
    })
    updateCarregamento()
}

//ATUALIZAR CARREGAMENTO
function updateCarregamento(){
    
    let novaLi = ''
    ListaDeCaregamento.forEach((item,posicao) => {
        novaLi = novaLi + `
        
        <div class="card">
            <header class="content">
                <nav>
                    <div class="menu">
                        <div><h1>SEQ</h1><span id="SEQ"></span>${posicao + 1}</div>
                        <div><h1>CLT</h1><span id="CLT"></span>${item.clt}</div>
                        <div class="motorista"><h1>MOTORISTA</h1><span id="MOT">${item.mot}</span></div>
                        <div class="destino"><h1>DESTINO</h1><span id="DEST">${item.dest}</span></div>
                        <div><h1>CONFERENTE</h1><span id="CONF">${item.conf}</span></div>
                        <div><h1>PLACA</h1><span id="PLACA">${item.placa}</span></div>
                        <div><h1>CUB</h1><span id="CUB">${item.cub}</span></div>
                    </div>
                </nav>

                <div class="logo">
                    <img src="/static/images.jpg" alt="Não a imagem" onclick="DeletarCarregamento(${posicao})">
                </div>
            </header>

            <div class="mae">

                <div class="${ClasseFase[0]}">
                    <div class="title">
                        <h1 onclick="CancelaAdia(${posicao})">EM ESPERA</h1>
                    </div>
                    <div class="passo">
                        <i class="${ClasseIcone[0]}" id="IconP1"></i>
                        <p id="MsgP1">separando mercadoria ou aguardando conferente!</p>
                    </div>
                </div>

                <div class="fase">
                    <div class="title" id="carregando">
                        <h1 onclick="salvardb()">CARREGANDO</h1>
                    </div>
                    <div class="passo">
                        <i class="bi bi-cone-striped" id="IconP2"></i>
                        <p id="MsgP2">Opa! jaja daremos o pontapé inicial...</p>
                    </div>
                </div>

                <div class="fase">
                    <div class="title" id="aguard-faturamento">
                        <h1>AGUARD FATURAMENTO</h1>
                    </div>
                    <div class="passo">
                        <i class="bi bi-cone-striped" id="IconP3"></i>
                        <p id="MsgP3">Parabéns! você avançou uma etapa do processo.</p>
                    </div>
                </div>

                <div class="fase">
                    <div class="title" id="faturando">
                        <h1>FATURANDO</h1>
                    </div>
                    <div class="passo">
                        <i class="bi bi-cone-striped" id="IconP4"></i>
                        <p id="MsgP4">Parabéns! você avançou uma etapa do processo.</p>
                    </div>
                </div>

                <div class="fase">
                    <div class="title" id="concluído">
                        <h1>CONCLUÍDO</h1>
                    </div>
                    <div class="passo">
                        <i class="bi bi-cone-striped" id="IconP5"></i>
                        <p class="MsgP5">Parabéns! você avançou uma etapa do processo.</p>
                    </div>
                </div>

            </div>

        </div>
    
        `
    })   
    listaCompleta.innerHTML = novaLi
    localStorage.setItem('lista', JSON.stringify(ListaDeCaregamento))
    SemCarregamento()
    
}

function DeletarCarregamento(posicao){
    ListaDeCaregamento.splice(posicao, 1)
    updateCarregamento()
}

function RecarregarCarregamento(){
    const CarregamentoLocalStorage = localStorage.getItem('lista')
    if (CarregamentoLocalStorage) {
        ListaDeCaregamento = JSON.parse(CarregamentoLocalStorage)
    }
    
    updateCarregamento()
    
}

/*FUNCÇÃO QUE ADIA OU CANCELA UM CARREGAMENTO*/
function CancelaAdia(posicao) {
    let AdiaCancela = 'CONCLUÍDO' /* VARIÁVEL QUE RECEBE O INPUT DO USUÁRIO*/
    let mae = listaCompleta.children[posicao].children[1]
    for (i = 0; i < mae.children.length + 1; i++){
        if (AdiaCancela ==  'CANCELADO') {
            mae.children[i].className = 'cancelado'
            mae.children[i].children[1].children[0].classList = canc
            mae.children[i].children[1].children[1].innerHTML = "CANCELADO!"     
        }
        if (AdiaCancela == 'ADIADO') {
            mae.children[i].className = 'adiado'
            mae.children[i].children[1].children[0].classList = circulo
            mae.children[i].children[1].children[1].innerHTML = 'ADIADO!'   
        }
        if (AdiaCancela == 'CONCLUÍDO') {
            mae.children[i].className = 'concluido'
            mae.children[i].children[1].children[0].classList = CHEKOK
            mae.children[i].children[1].children[1].innerHTML = 'CONCLUÍDO!'
        }
        
    }
}

 function SemCarregamento(){
    if (ListaDeCaregamento != ''){
        NoCarregamento.innerHTML = ''; 
    }
    else{
        NoCarregamento.innerHTML = 'NÃO À CARREGAMENTO NESSE MOMENTO!!!'; 
    }
 }

 RecarregarCarregamento()