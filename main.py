from database import consultarDados
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():

    dados = consultarDados()
    return render_template("index.html", registro=dados)


@app.route("/addCarregamento", methods=["post"])
def eddCarregamento():
    clt = request.form.get('clt')
    print(clt)


if __name__ == '__main__':
    app.run(debug=True)
