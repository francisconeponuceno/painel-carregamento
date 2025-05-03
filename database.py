import sqlite3
import string


# FUNÇÃO PARA CRIAR A TABELA CARREGO
def CriarTabela_Carrego():
    try:
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
            status TEXT,
            img TEXT
            );
        """)
        conect.close()
        print('TABELA CRIADA COM SUCESSO')
    except:
        print('ERRO AO CRIAR A TABELA')


def salvar(clt,mot,dest,conf,placa,cub,status,img):
    try:
        conect = sqlite3.connect('banco.db')
        cursor = conect.cursor()
        cursor.execute('''INSERT INTO carrego(clt, mot, dest, conf, placa, cub, status, img) VALUES(?,?,?,?,?,?,?,?)''',          
        [clt, mot, dest, conf, placa, cub, status, img])
        conect.commit()
        conect.close()
        print('DADOS SALVO COM SUCESSO')
    except:
        print('ERRO AO SALVAR OS DADOS')

# FUNÇÃO PARA CONSULTAR OS DADOS
def consultarDados():
    try:
        conect = sqlite3.connect('banco.db')
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM carrego')
        registros = cursor.fetchall()
        conect.close()
        return registros
    except:
        print('ERRO AO CONSULTAR OS DADOS')

def indicadores():
    conct = sqlite3.connect('banco.db')
    cursor = conct.cursor()
    cursor.execute('SUM')

# FUNÇÃO PARA ALTERAR OS DADOS
def alterarFase(id,fase):
    try:
        conect = sqlite3.connect('banco.db')
        cursor = conect.cursor()
        cursor.execute(f"UPDATE carrego SET status = '{fase}' WHERE id = {id} ")
        conect.commit()
        conect.close()
        print('DADOS ALTERADO COM SUCESSO')
    except:
        print('ERRO AO ALTERAR OS DADOS')


# FUNÇÃO PARA EXCLUIR REGISTROS
def excluir(id):
    try:
        conect = sqlite3.connect('banco.db')
        cursor = conect.cursor()
        cursor.execute(f'DELETE FROM carrego WHERE id = {id}')
        conect.commit()
        conect.close()
    except:
        print('ERRO AO EXCLUIR OS DADOS')





#CriarTabela_Carrego()

#salvar('T','SILVAN ALVES CHAVES','FORTALEZA','CASSIO','QRZ-2B31','80','AGUARD','img/socimol.png')

#alterarFase(1,'img/img_fabio.png')


