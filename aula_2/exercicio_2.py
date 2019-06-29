# -*- coding: utf-8 -*-
# Escrever um método que calcula a raiz quadrada
# de um número 
# A raiz quadrada só é definida para números
# positivos, logo se o valor for menor do que 
# zero levantem uma exceção

def calcular_raiz(x):
	if x < 0:
		raise Exception()
	return x ** (0.5)

try:
	res = calcular_raiz(3)
except:
	print('Erro')
# res = calcular_raiz(-2)
print(res)

def A():
	print('A')
	try:
		B()
	except:
		print('Erro capturado na A')
	C()

def B():
	print('B')
	E()
	D()

def C():
	print('C')

def D():
	print('D')	

def E():
	print('E')
	raise Exception()

A()