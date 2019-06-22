
opcao = None
while opcao != '3':
	print('1 - Cadastrar novo usuário')
	print('2 - Ver usuários cadastrados')
	print('3 - Sair')
	opcao = input('Selecione uma das opções: ')
print('Fim das opções')

numero = input('Digite um número: ')
while not numero.isnumeric():
	numero = input('Digite um número: ')

print(numero)