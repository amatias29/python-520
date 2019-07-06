# -*- coding: utf-8 -*-

# Criar uma class Usuario que tenha
# os atributos nome, idade, email
# e os métodos:
# - maior de idade
# - funcionario da 4linux
# - tem moto

class Usuario:

	def __init__(self, nome, email, idade):
		self.nome = nome
		self.idade = idade
		self.email = email

	def maior_de_idade(self):
		if self.idade >= 18:
			return True
		else:
			return False

	def func_4linux(self):
		if '@4linux' in self.email:
			return True
		else:
			return False

	def tem_moto(self):
		if self.nome == 'Lucas':
			return True
		else:
			return False

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
idade = int(input('Digite sua idade: '))

user1 = Usuario(nome, email, idade)

print('Olá {}'.format(user1.nome))

print(user1.maior_de_idade())
print(user1.func_4linux())
print(user1.tem_moto())

exit()

class Lampada:

	acesa = False

	def pressionar_interruptor(self):
		self.acesa = not self.acesa


lampada1 = Lampada()
lampada2 = Lampada()

opcao = input('Deseja acender a lâmpada? (S/N) ')
if opcao == 'S':
	lampada1.pressionar_interruptor()

print('Lâmpada 1: ' + str(lampada1.acesa))
print('Lâmpada 2: ' + str(lampada2.acesa))
