from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///server.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")

class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable = False)
    idade = Column('IDADE', Integer, nullable = False)
    salario = Column('SALARIO', Float, nullable = False)

    def __init__(self, nome, idade, salario): 
        self.nome = nome
        self.idade = idade
        self.salario = salario

# func1 = Funcionario('Luizinho', 22, 1250)
# func2 = Funcionario('Huguinho', 24, 2200)
# func3 = Funcionario('Douglas', 30, 12300)
# lista = [func1, func2, func3]
# session.add_all(lista)
# session.commit()

print('------'*15)
func1 = session.query(Funcionario)
for obj in func1:
    print(obj.id, obj.nome, obj.idade, obj.salario)

print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)
