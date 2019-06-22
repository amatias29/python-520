# tipos primitivos
string = 'Alberto'
inteiro = 32
flutuante = 150000.92
booleano = True

# estruturas de dados
tupla = (1, 2, 3, 4)
lista = [1, 2, 3, 4]
dicionario = {
	'nome': 'Alberto',
	'idade': 32
}

# ex1: Criar uma estrutura que armazena:
# - Nome, idade, e-mail, sexo, altura e peso

'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
email = input('Digite seu e-mail: ')
sexo = input('Digite o sexo: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')


usuario = {
	'nome': nome,
	'idade': idade,
	'email': email,
	'sexo': sexo,
	'altura': altura,
	'peso': peso
}

'''
usuario = {
	'nome': input('Digite seu nome: '),
	'idade': input('Digite sua idade: '),
	'email': input('Digite seu e-mail: '),
	'sexo': input('Digite o sexo: '),
	'altura': input('Digite sua altura: '),
	'peso': input('Digite seu peso: ')
}

#print(usuario)

# ex2: Imprimir no terminal SOMENTE
# o nome e a idade digitadas

print(usuario['nome'])
print(usuario['idade'])