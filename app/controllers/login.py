from app import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST']) #/login or /anything
def login():
    if request.method == 'GET':
        pass
    
    if request.method == 'POST': 
        login = request.form.get('login')
        senha = request.form.get('senha')
        login(login, senha)
        
    return render_template('login.html');
