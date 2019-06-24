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
        PRIMARY KEY (idAutor, idLivro)
        FOREIGN KEY (idAutor) REFERENCES autor(idAutor),
        FOREIGN KEY (idLivro) REFERENCES livro(idLivro)
);

CREATE TABLE IF NOT EXISTS livro(
    idLivro integer PRIMARY KEY autoincrement,
    isbn integer NOT NULL,
    titulo text NOT NULL,
    precoVenda real NOT NULL,
    formato text NOT NULL,
    idEditora integer NOT NULL,
    precoCusto real NOT NULL,
    margemLucro real NOT NULL,
    avaliacao real NOT NULL,
    quantidadeEstoque integer NOT NULL,
    capa BLOB NOT NULL,
        FOREIGN KEY (idEditora) REFERENCES editora(idEditora)
);

CREATE TABLE IF NOT EXISTS editora(
    idEditora integer PRIMARY KEY autoincrement,
    nomeEditora text NOT NULL,
    cnpj text NOT NULL,
    endereco text NOT NULL,
    telefone integer NOT NULL    
);
