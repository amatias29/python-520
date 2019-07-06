
import pymongo

client = pymongo.MongoClient()
db = client.projeto


def cadastrar_usuario(nome, email, idade):
	db.usuarios.insert({
		'nome': nome,
		'email': email,
		'idade': idade
	})


def listar_usuarios():
	return list(u for u in db.usuarios.find())

if __name__ == '__main__':


	nome = input('Digite seu nome: ')
	email = input('Digite seu e-mail: ')
	idade = input('Digite sua idade: ')

	cadastrar_usuario(nome, email, idade)

	for usuario in listar_usuarios():
		print(usuario)
