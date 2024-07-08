from database import consultarDados
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():

    dados = consultarDados()
    return render_template("index.html", registro=dados)


@app.route('/cadastrar',methods=['POST','GET'])
def cadastrar():
    CLT = request.form['clt']
    print(CLT)
    return render_template("index.html")


    
if __name__ == '__main__':
    app.run(debug=True)

