from flask import Flask, render_template, request
from flask_cors import CORS
from models import *

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST']) #/login or /anything
def index();
    if request.method == 'GET':
        pass
    
    if request.method == 'POST': #modificar isso para o contexto da livraria
        login = request.form.get('login')
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')
        endereco = request.form.get('endereco')
        register(login, nome, email, senha, cpf, endereco)
        
    return render_template('index.html');

if __name__ == '__main__':
    app.run(debug=True)
    