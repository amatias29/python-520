# -*- coding: utf-8 -*-

import json
import time

BANCO_DE_DADOS = []

FORMATO = '{%Y-%m-%d %H:%M:%S}'
class Usuario:

	def __init__(self, nome, email, idade):
		self.nome = nome
		self.email = email
		self.idade = idade
		self.data_criacao = time.strftime(FORMATO)

	def to_json(self):
		return {
			'nome': self.nome,
			'email': self.email,
			'idade': self.idade,
			'data_criacao': self.data_criacao
		}

	def __repr__(self):
		return json.dumps(self.to_json(), indent=2)



def cadastrar_usuario():

	global BANCO_DE_DADOS

	nome = input('Digite seu nome: ')
	email = input('Digite seu email: ')
	idade = input('Digite sua idade: ')

	usuario = Usuario(nome, email, idade)

	BANCO_DE_DADOS.append(usuario)

	with open('banco.json', 'w') as f:
		f.write(
			json.dumps(
				[ u.to_json() for u in BANCO_DE_DADOS ], indent=2
			),			
		)

def consultar_usuario(email):
	usuarios_salvos = []
	with open('banco.json', 'r') as f:
		usuarios_salvos = json.loads(
			''.join(f.readlines())
		)

	print(usuarios_salvos)

def excluir_usuario(email):
	pass

def gerar_csv():
	pass

cadastrar_usuario()

consultar_usuario('aaa')
