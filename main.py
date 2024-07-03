from database import consultarDados
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    dados = consultarDados()
    return render_template("index.html", registro=dados)
    

if __name__ == '__main__':
    app.run(debug=True)

