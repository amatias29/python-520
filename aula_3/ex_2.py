import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
	dbname='projeto',
	user='admin',
	password='4linux',
	host='localhost',
	port='5432'
)

cursor = conn.cursor(
	cursor_factory=psycopg2.extras.RealDictCursor
)

def cadastrar_usuario(nome, email, idade):
	query = '''

		INSERT INTO usuarios (nome, email, idade)
		VALUES ('{}', '{}', '{}');

	'''.format(nome, email, idade)

	cursor.execute(query)
	conn.commit()


def relacionar_time_usuario(torcedor, time):
	query = '''

		INSERT INTO rel_usuarios_times (usuario, time)
		VALUES ('{}', '{}');

	'''.format(torcedor, time)

	cursor.execute(query)
	conn.commit()


def listar_usuarios(email):
	query = '''

		SELECT * FROM usuarios
		WHERE email like '%{}%';

	'''.format(email)

	cursor.execute(query)
	return cursor.fetchall()


def listar_times():
	query = '''

		SELECT id, nome FROM times;

	'''

	cursor.execute(query)
	return cursor.fetchall()


if __name__ == '__main__':

	email = input('Digite seu e-mail: ')

	for usuario in listar_usuarios(email):
		print(usuario['nome'])

	exit()

	nome = input('Digite seu nome: ')
	email = input('Digite seu e-mail: ')
	idade = input('Digite sua idade: ')

	for time in listar_times():						
		print(time['id'], ' - ', time['nome'])

	time_selecionado = input('Selecione o time do Goku: ')

	relacionar_time_usuario(3, time_selecionado)




	exit()

	cadastrar_usuario(nome, email, idade)