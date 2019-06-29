# -*- coding: utf-8 -*-

def receber_inteiro3(mensagem):
	while True:
		valor = input(mensagem)
		try:
			return int(valor)
		except ValueError:
			print('Número inválido')		

res = receber_inteiro3('Digite um número: ')
print(res)

exit()

def receber_inteiro2(mensagem):
	valor = input(mensagem)
	try:
		return int(valor)
	except ValueError:
		val = receber_inteiro2(mensagem)
		return val
	

res = receber_inteiro2('Digite um número: ')
print(res)

exit()

def receber_inteiro(mensagem):
	valor = input(mensagem)
	return int(valor)
	
try:
	res = receber_inteiro('Digite um número: ')
	print(res)
except ValueError:
	print('Erro ao inserir número')
except Exception as e:
	raise e

exit()

# Exemplo

def fn(index, key, string):

    x = [ 1, 2, 3 ]
    y = { 'nome': 'Lucas' }

    x[index]
    y[key]
    int(string)

    print('DEU TUDO CERTO AQUI')

def capturar_execao(function, *args):
    try:
        function(*args)
    except IndexError:
        print('Capturado erro no indice')
    except KeyError:
        print('Capturado erro na chave')
    except ValueError:
        print('Capturado erro na conversão para inteiro')
    except Exception:
        print('Erro capturado')

capturar_execao(fn, 2, 'nome', '55')        #ok
capturar_execao(fn, 3, 'nome', '55')        #e1
capturar_execao(fn, 2, 'idade', '55')       #e2
capturar_execao(fn, 2, 'nome', 'lucas')     #e3

# fn(3, 'nome', '55')     # index error
# fn(2, 'idade', '55')    # key error
# fn(2, 'nome', 'lucas')  # value error 
