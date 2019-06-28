from app import db
from datetime import datetime

autoria = db.Table('autoria',
    db.Column('idautor', db.Integer, db.ForeingnKey('autor.id', primary_key=True)),
    db.Column('idlivro', db.Integer, db.ForeingnKey('livro.id', primary_key=True))
)

categorizacao = db.Table('categorizacao',
    db.Column('idcategoria', db.Integer, db.ForeingnKey('categoria.id', primary_key=True)),
    db.Column('idlivro', db.Integer, db.ForeingnKey('livro.id', primary_key=True))
)
class Livro(db.Model):
    __tablename__ = "livro"

    id = db.Column(db.Integer, primary_key=True)
    ideditora = db.Column(db.Integer, db.ForeingnKey('editora.id'), nullable=False)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    edicao = db.Column(db.Integer, nullable=False)
    precoVenda = db.Column(db.Real, nullable=False)
    precoCusto = db.Column(db.Real)
    margemLucro = db.Column(db.Real)
    avaliacao = db.Column(db.Real)
    quantidadeEstoque = db.Column(db.Integer, nullable=False)
    numeroPaginas - db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(120), unique=True, nullable=False)
    formato = db.Column(db.String(20), nullable=False)
    sinopse = db.Column(db.String, nullable=False)
    capa = db.Column(db.LargeBinay)
    autores = db.relashionship('Autor', secondary=autoria,
        backref=db.backref('livros', lazy='dynamic'))
    categorias = db.relashionship('Categoria', secondary=categorizacao,
        backref=db.backref('livros', lazy='dynamic'))
    #email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, editora, isbn, edicao, precoVenda, quantidadeEstoque, titulo, formato, sinopse):
        self.editora = editora
        self.edicao = edicao
        self.precoVenda = precoVenda
        self.quantidadeEstoque = quantidadeEstoque
        self.titulo = titulo
        self.formato = formato
        self.sinopse = sinopse

    def __repr__(self):
        return "<Livro %r>" % self.titulo

class Categoria(db.Model):
    __tablename__ = "categoria"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "<Categoria %r>" % self.nome

class Editora(db.Model):
    __tablename__ = "editora"

    id = db.Column(db.Integer, primary_key=True) #uma editora pode ter mto livros
    cnpj = db.Column(db.Integer)
    telefone = db.Column(db.Integer)
    nome = db.Column(db.String(140), nullable=False)
    endereco = db.Column(db.String)
    livros = db.relashionship('Livro', lazy='select',
        backref=db.backref('editora', lazy='joined'))

    def __init__(self, cnpj, nome, telefone, endereco):
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(sel):
        return "<Editora %r>" % self.nome

class Autor(db.Model):
    __tablename__ = "autor"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    localMorte = db.Column(db.String)
    localNascimento = db.Column(db.String)
    biografia = db.Column(db.String)
    dataFalescimento = db.Column(db.DateTime)

    def __init__(self, nome, localNascimento, biografia):
        self.nome = nome
        self.localNascimento = localNascimento
        self.biografia = biografia

    def __repr__(self):
        return "<Autor %r>" % self.nome


class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    endereco = db.Column(db.String, nullable=False)
    cpf = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, login, senha, email, endereco, cpf):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        self.endereco = endereco
        self.cpf = cpf

    def __repr__(self):
        return "<Cliente %r>" % self.nome
