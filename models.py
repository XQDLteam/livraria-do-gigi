import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))
con = sql.connect(path.join(ROOT, 'livraria.db'))
cur = con.cursor()

#adicionar funcionalidades
def register(login, nome, email, senha, cpf, endereco):
    with con:
        cur.execute("INSERT INTO cliente (login, nome, email, senha, cpf, endereco) values (?, ?, ?, ?, ?, ?)", 
                     (login, nome, email, senha, cpf, endereco))

    con.commit()
    con.close()
