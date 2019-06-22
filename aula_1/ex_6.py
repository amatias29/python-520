
def receber_inteiro(mensagem):
	valor = input(mensagem)
	if valor.isnumeric():
		return int(valor)
	print('Número inválido')
	exit()

def receber_inteiro2(mensagem):
	valor = input(mensagem)
	while not valor.isnumeric():
		valor = input(mensagem)
	return int(valor)


usuario = {
	'nome': input('Digite seu nome: '),
	'idade': receber_inteiro2('Digite sua idade: '),
	'peso': receber_inteiro2('Digite seu peso: ')
}