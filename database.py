import sqlite3


def criarTabela():
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
        classe TEXT,
        icone TEXT,
        frase TEXT
        );
    """)
    conect.close()

# Inserir um novo usuário
Dados = ['T', 'JOAQUIM MAIA PEREIRA', 'MARANHÃO',  'FABIO', 'KBI-6155', '80','fase','bi bi-truck','']
def salvar(clt,mot,dest,conf,placa,cub,classe,icone,frase):
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    
    cursor.execute(f"INSERT INTO carrego(clt, mot, dest, conf, placa, cub, classe, icone, frase) VALUES(?,?,?,?,?,?,?,?,?)", [clt,mot,dest,conf,placa,cub,classe,icone,frase])
    conect.commit()
    conect.close()     


#Consultar dados
def consultarDados():
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute('SELECT * FROM carrego')
    registros = cursor.fetchall()
    return registros

    
#alterar dados 
def alterarDados():
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute(f'UPDATE carrego WHERE id = {id}')
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

criarTabela()
#salvar(Dados[0],Dados[1],Dados[2],Dados[3],Dados[4],Dados[5],Dados[6],Dados[7],Dados[8])