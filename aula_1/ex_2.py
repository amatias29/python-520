
usuario = {
	'nome': 'Belzebu',
	'email': 'bel@zebu.com',
	'idade': '5000'
}

condicao = True
if condicao:
	print('Verdade')
else:
	print('Falso')

print('sempre imprime isso')

# ex3 dado o usuário acima,
# se a idade dele dividida por 5
# for maior do que 1200
# imprimir "Você é velho"

if (int(usuario['idade'])/5) > 1200:
	print('Você é velho')
else:
	print('Você não é velho')


# ex4 se o e-mail do usuário acima
# não conter um '@' imprimir email inválido

'''
if usuario['email'].find('@') != -1:
	print('E-mail correto')
else:
	print('E-mail incorreto')
'''

if '@' not in usuario['email']:
	print('E-mail inválido')
else:
	print('E-mail válido')

idade = input('Digite a idade: ')

for x in idade:
	if x not in '0123456789':		
		erro = True
		break
	else:
		erro = False
if erro:
	print('Erro, a idade não é um número!')
else:
	print('A idade é:', idade)

if not idade.isnumeric:
	erro = True
else:
	erro = False
if erro:
	print('Erro, a idade não é um número!')
else:
	print('A idade é:', idade)
