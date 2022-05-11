import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///servidor.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable=False)
    paginas = Column('PAGINAS', Integer, nullable=False)
    autor_id = Column('AUTOR_ID', Integer, nullable=False)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor('Paulo Vieira')
autor2 = Autor('Maria da Silva')
session.add(autor1)
session.add(autor2)
session.commit()

livro1 = Livro('Titulo do Livro 1', 300, autor1.id)
livro2 = Livro('Titulo do Livro 2', 150, autor2.id)
session.add(livro1)
session.add(livro2)
session.commit()

# consulta de autores
print('----------------------------------')
lista = session.query(Autor)
for a in lista:
    print(a.id, a.nome)

# consulta de livros
print('----------------------------------')
lista = session.query(Livro)
for a in lista:
    print(a.id, a.titulo, a.paginas, a.autor_id)

# Exemplo de join (relação entre duas tabelas)
print('----------------------------------')
lista = session.query(Livro, Autor).filter(Livro.autor_id == Autor.id)
for a in lista:
    print(a.Autor.nome, a.Livro.titulo)

connection.close()