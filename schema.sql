CREATE TABLE IF NOT EXISTS autor(
  idAutor integer PRIMARY KEY autoincrement,
  nomeAutor text NOT NULL, 
  dataFalescimento text,
  localMorte text, 
  localNascimento text NOT NULL,
  biografia text NOT NULL
);

CREATE TABLE IF NOT EXISTS autoria(
  idAutor integer,
  idLivro integer,
  PRIMARY KEY (idAutor, idLivro),
  FOREIGN KEY (idAutor) REFERENCES autor(idAutor),
  FOREIGN KEY (idLivro) REFERENCES livro(idLivro)
);

CREATE TABLE IF NOT EXISTS livro(
  idLivro integer PRIMARY KEY autoincrement,
  isbn integer NOT NULL,
  titulo text NOT NULL,
  numeroPaginas integer NOT NULL,
  edicao integer NOT NULL,
  precoVenda real NOT NULL,
  formato text NOT NULL,
  idEditora integer,
  precoCusto real NOT NULL,
  margemLucro real NOT NULL,
  avaliacao real NOT NULL,
  sinopse text NOT NULL,
  quantidadeEstoque integer NOT NULL,
  capa BLOB,
    FOREIGN KEY (idEditora) REFERENCES editora(idEditora)
);

CREATE TABLE IF NOT EXISTS editora(
  idEditora integer PRIMARY KEY autoincrement,
  nomeEditora text NOT NULL, 
  cnpj text NOT NULL,
  endereco text NOT NULL, 
  telefone integer NOT NULL
);

CREATE TABLE IF NOT EXISTS compra(
  idCompra integer PRIMARY KEY autoincrement,
  precoTotal real CHECK(precoTotal > 0.0)
);
CREATE TABLE IF NOT EXISTS item(
  idCompra integer,
  idLivro integer,
  quantidade integer,
  precoPago real CHECK(precoPago > 0.0),
  PRIMARY KEY (idCompra, idLivro),
    FOREIGN KEY (idCompra) REFERENCES compra(idCompra),
    FOREIGN KEY (idLivro) REFERENCES livro(idLivro)
);
CREATE TABLE IF NOT EXISTS cliente(
  idCliente integer PRIMARY KEY autoincrement,
  login text NOT NULL, 
  nome text NOT NULL,
  email text NOT NULL, 
  cpf integer NOT NULL,
  senha text NOT NULL, 
  endereco text NOT NULL
);

CREATE TABLE IF NOT EXISTS funcionario(
  idFuncionario integer PRIMARY KEY autoincrement,
  login text NOT NULL, 
  nome text NOT NULL,
  senha text NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidoCliente(
  idCompra integer,
  idCliente integer,
  notaFiscal integer NOT NULL,
  enderecoNotaFiscal text NOT NULL,
  valorNotaFiscal real NOT NULL,
  estadoPedido text NOT NULL,
    PRIMARY KEY (idCompra, idCliente),
    FOREIGN KEY (idCompra) REFERENCES compra(idCompra),
    FOREIGN KEY (idCliente) REFERENCES cliente(idCliente)
);

CREATE TABLE IF NOT EXISTS pedidoEditora(
  idCompra integer,
  notaFiscal integer NOT NULL,
  valorNotaFiscal real NOT NULL,
  estadoPedido text NOT NULL,
    PRIMARY KEY (idCompra),
    FOREIGN KEY (idCompra) REFERENCES compra(idCompra)
);
