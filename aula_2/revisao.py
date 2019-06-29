# escrever uma função chamada maximo que
# recebe três números e retorna qual deles
# é o MAIOR

def maximo(a, b, c):
	'''
	if (a >= b) and (a >= c):
		print('O maior número é o: ' + str(a))
	elif (b >= a) and (b >= c):
		print('O maior número é o: ' + str(b))
	else:
		print('O maior número é o: ' + str(c))
	'''
	return max(a, max(b, c))

num1 = input('Digite um número: ')
while not num1.isnumeric():
	num1 = input('Digite um número: ')
num2 = input('Digite um número: ')
while not num2.isnumeric():
	num2 = input('Digite um número: ')
num3 = input('Digite um número: ')
while not num3.isnumeric():
	num3 = input('Digite um número: ')

maior = maximo(num1, num2, num3)
print('O maior número é o: ' + str(maior))


# escrever uma função mult_lista
# que recebe uma lista de números
# e retorna a multiplicação deles todos

# ex: mult_lista([1, 2, 3, 4])

def mult_lista(lista_de_num):
	resultado = 1
	for i in lista_de_num:
		resultado *= i

	return resultado

lista_de_num = [1, 2, 3, 4]

res = mult_lista(lista_de_num)
print(res)

# escrever uma função que recebe uma string
# (um nome por exemplo) e retorna o número
# de caracteres minúsculos e número de caracteres
# maiúsculos, chame ela de contador

def contador(string):
	maiusculas, minusculas = [], []	
	for i in string.replace(' ', ''):
		if i.islower():
			minusculas.append(i)		
		else:
			maiusculas.append(i)
	return maiusculas, minusculas

maiusculas, minusculas = contador('Alberto N Matias')
print(maiusculas, minusculas)

