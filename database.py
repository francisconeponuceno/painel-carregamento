import sqlite3


#conectar ao banco
def banco():
    conect = sqlite3.connect('banco.db')
    conect = conect.cursor()
    return conect


def TabCarrego():
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS carrego (     
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        clt TEXT,
        mot TEXT,
        dest TEXT,
        conf TEXT,
        placa TEXT,
        cub INTEGER,
        classe1 TEXT,
        classe2 TEXT,
        classe3 TEXT,
        classe4 TEXT,
        classe5 TEXT,
        icone1 TEXT,
        icone2 TEXT,
        icone3 TEXT,
        icone4 TEXT,
        icone5 TEXT,
        frase1 TEXT,
        frase2 TEXT,
        frase3 TEXT,
        frase4 TEXT,
        frase5 TEXT
        );
    """)
    conect.close()


# Inserir um novo usuário
Dados = ['C', 'JOAQUIM MAIA PEREIRA', 'MARANHÃO / PARÁ / TOCANTINS',  'FABIO', 'KBI-6155', '80',
         'fase','fase','fase','fase','fase',
         'bi bi-truck','bi bi-cone-striped','bi bi-cone-striped','bi bi-cone-striped','bi bi-cone-striped',
         'EM ESPERA','CARREGANDO','AGUAR FATURAMENTO','FATURANDO','CONCLUÍDO']

def salvar(clt,mot,dest,conf,placa,cub,casse1,classe2,classe3,classe4,classe5,
           icone1,icone2,icone3,icone4,icone5,frase1,frase2,frase3,frase4,frase5):
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute('''INSERT INTO carrego(clt, mot, dest, conf, placa, cub,
                   classe1, classe2, classe3, classe4, classe5,
                   icone1, icone2, icone3, icone4, icone5,
                   frase1, frase2, frase3, frase4, frase5) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                   [clt,mot,dest,conf,placa,cub,casse1,classe2,classe3,classe4,classe5,
                    icone1,icone2,icone3,icone4,icone5,frase1,frase2,frase3,frase4,frase5])
    conect.commit()
    conect.close()

#Consultar dados
def consultarDados():
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute('SELECT * FROM carrego')
    registros = cursor.fetchall()
    conect.close()
    return registros
    

    
#alterar dados 
def alterarFase(id,fase):
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    if fase == 1:
        cursor.execute(f"UPDATE carrego SET classe = 'concluido', icone = 'bi bi-check2-circle', frase = 'CONCLUÍDO' WHERE id = {id}")

    conect.commit()
    conect.close()


#excluír registro
def excluir(id):
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute(f'DELETE FROM carrego WHERE id = {id}')
    conect.commit()
    conect.close()


#eliminando a tabela
def eliminaTabela():
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute(f'DROP TABLE carrego')
    conect.commit()
    conect.close()

#eliminaTabela()
TabCarrego()


#salvar(Dados[0],Dados[1],Dados[2],Dados[3],Dados[4],Dados[5],
       #Dados[6],Dados[7],Dados[8],Dados[9],Dados[10],Dados[11],
       #Dados[12],Dados[13],Dados[14],Dados[15],Dados[16],Dados[17],
       #Dados[18],Dados[19],Dados[20])

#alterarFase(5,1)


