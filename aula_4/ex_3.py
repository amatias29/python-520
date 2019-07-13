
# Criar uma tabela de times que contenha as colunas
# nome,
# estadio,
# ano_de fundacao

import datetime
import hashlib

import sqlalchemy

URL = 'sqlite:///teste.db'
engine = sqlalchemy.create_engine(URL, echo=True)

metadata = sqlalchemy.MetaData(bind=engine)

time_table = sqlalchemy.Table(
	'times',
	metadata,
	sqlalchemy.Column(
		'id', 
		sqlalchemy.Integer, 
		primary_key=True
	),
	sqlalchemy.Column(
		'nome', 
		sqlalchemy.String(40), 
		index=True,
	),
	sqlalchemy.Column(
		'estadio', 
		sqlalchemy.String, 
		nullable=False
	),
	sqlalchemy.Column(
		'ano_de_fundacao', 
		sqlalchemy.Integer 		
	),
	sqlalchemy.Column(
		'criado_em', 
		sqlalchemy.DateTime, 
		default=datetime.datetime.now
	),
	sqlalchemy.Column(
		'atualizado_em', 
		sqlalchemy.DateTime, 
		default=datetime.datetime.now,
		onupdate=datetime.datetime.now
	)

)

metadata.create_all(engine)

con = engine.connect()
insert = time_table.insert()

con.execute(
	insert.values(
		nome='Nacional',
		estadio='Comendador Souza',
		ano_de_fundacao=1919
	)
)

for result in sqlalchemy.select([ time_table ]).execute():
    print(result)