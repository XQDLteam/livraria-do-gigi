from flask import Flask, render_template, request
from flask_cors import CORS
from models import *
import os

app = Flask(__name__)
#app._static_folder=os.path.abspath("templates/css/login.css")
#app._static_folder=os.path.abspath("templates/css/base.css")
CORS(app)
@app.route('/', methods=['GET', 'POST']) #/login or /anything
def index():
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
        
    return render_template('login.html');

if __name__ == '__main__':
    app.run(debug=True)
    
