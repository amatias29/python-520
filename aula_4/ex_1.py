
import datetime
import hashlib

import sqlalchemy

URL = 'sqlite:///teste.db'
engine = sqlalchemy.create_engine(URL, echo=True)

metadata = sqlalchemy.MetaData(bind=engine)

user_table = sqlalchemy.Table(
	'usuarios',
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
		'idade', 
		sqlalchemy.Integer, 
		nullable=False
	),
	sqlalchemy.Column(
		'senha', 
		sqlalchemy.String 		
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
insert = user_table.insert()

'''
con.execute(
	insert.values(
		idade=32,
		nome='Alberto',
		senha='4linux'
	)
)

for result in sqlalchemy.select([ user_table ]).execute():
    print(result)
'''

def cadastrar_usuario(nome, idade, senha):
	con.execute(
		insert.values(
			idade=idade,
			nome=nome,
			senha=hashlib.md5(senha.encode('utf-8')).hexdigest()
		)
	)

'''
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
senha = input('Digite sua senha: ')

cadastrar_usuario(nome, idade, senha)

for result in sqlalchemy.select([ user_table ]).execute():
    print(result)
'''

res = sqlalchemy.update(user_table).where(
	user_table.c.nome == 'Alberto'
).values(nome='Alberto Matias').execute()

print(res.rowcount)

for result in sqlalchemy.select([ user_table ]).execute():
    print(result)

def selecionar_usuarios_por_idade():
	idade = int(input('Digite uma idade: '))

	res = len(sqlalchemy.select([ user_table ]).where(
		user_table.c.idade == idade
	).execute().fetchall())

	res = len([ r for r in sqlalchemy.select([ user_table ]).where(
		user_table.c.idade == idade
	).execute().fetchall() ])

	print('Temos {} usuarios com idade de {} anos'.format(res, idade))	

selecionar_usuarios_por_idade()

res = sqlalchemy.delete(user_table).where(
		user_table.c.idade == 22
	).execute()

print('{} usuarios deletados'.format(res))	


