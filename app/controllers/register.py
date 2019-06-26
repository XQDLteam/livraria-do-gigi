from app import app
from flask import render_template, request
from app.models import *

@app.route('/', methods=['GET', 'POST']) #/login or /anything
def cadastro():
    if request.method == 'GET':
        pass
    
    if request.method == 'POST': 
        login = request.form.get('login')
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')
        endereco = request.form.get('endereco')
        register(login, nome, email, senha, cpf, endereco)
        
    return render_template('cadastro.html');
