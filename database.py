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
        cub INTEGER
        );
    """)
    conect.close()

# Inserir um novo usuário
def salvar():
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    Dados = ['T', 'ELISVALDO DA ROCHA SILVA', 'BAHIA / GOIÁS / BRASÍLIA / MINAS GERAIS',  'CASÉ', 'GLV-7719', '82']
    cursor.execute(f"INSERT INTO carrego(clt, mot, dest, conf, placa, cub) VALUES(?,?,?,?,?,?)", [Dados[0],Dados[1],Dados[2],Dados[3],Dados[4],Dados[5]])
    conect.commit()
    conect.close()     


#Consultar dados
def consultarDados():
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute('SELECT * FROM carrego')
    registros = cursor.fetchall()
    return registros

    
#excluír registro
def excluir(id):
    conect = sqlite3.connect('banco.db')
    cursor = conect.cursor()
    cursor.execute(f'DELETE FROM carrego WHERE id = {id}')
    conect.commit()
    conect.close()


salvar()