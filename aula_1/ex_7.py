
BANCO_DE_DADOS = []

def cadastrar_usuario(usuario):
	global BANCO_DE_DADOS
	BANCO_DE_DADOS.append(usuario)

def consultar_usuario(email):
	for usuario in BANCO_DE_DADOS:
		if usuario['email'] == email:
			return usuario
	return None

def receber_input(mensagem, bloquear=False):
	if not bloquear:
		valor = input(mensagem)
		if not valor.isnumeric():
			exit()
		return int(valor)
	else:
		valor = ''
		while not valor.isnumeric():
			valor = input(mensagem)
		return int(valor)

mensagem = 'duasidhuas'
receber_input(mensagem, bloquear=True)
receber_input(mensagem)