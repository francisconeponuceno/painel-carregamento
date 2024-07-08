from database import consultarDados
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():

    dados = consultarDados()
    return render_template("index.html", registro=dados)


<<<<<<< HEAD
@app.route('/cadastrar',methods=['POST','GET'])
def cadastrar():
    CLT = request.form['clt']
    print(CLT)
    return render_template("index.html")


    
=======
@app.route("/addCarregamento", methods=["post"])
def eddCarregamento():
    clt = request.form.get('clt')
    print(clt)


>>>>>>> a712e0694401f30755da623f3831f745cda73b76
if __name__ == '__main__':
    app.run(debug=True)
