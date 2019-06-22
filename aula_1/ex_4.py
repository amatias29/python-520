
# situação:
# você é um professor e quer automatizar
# o cálculo das médias de sua turma.
# Seu programa deve receber:
# 1 - Número de avaliações aplicadas
# 2 - para cada avaliação, digite a nota do aluno
# Ao final, calcular a média das avaliações
# e se a média for maior do que 6, imprimir
# APROVADO,
# se não REPROVADO

num_aval = int(input('Digite o número de avaliações: '))
#while not num_aval.isnumeric:
#	num_aval = input('Digite o número de avaliações: ')

lista_avaliacoes = []

for i in range(num_aval):
	n = i + 1
	nota = input('Digite a nota da avaliação ' + str(n) + ': ')
	while not nota.isnumeric():
		nota = input('Digite a nota da avaliação ' + str(n) + ': ')
	lista_avaliacoes.append(int(nota))

tot_nota = 0
for i in lista_avaliacoes:
	tot_nota += i

media = sum(lista_avaliacoes) / num_aval

if media >= 6:
	print('Aprovado com média {}'.format(media))
else:
	print('Reprovado com média {}'.format(media))

print('Média:', tot_nota/num_aval)

