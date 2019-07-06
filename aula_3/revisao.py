class ContaBancaria:

	def __init__(self):
		self.saldo = 0
		self.rendimento = 0.05

	def depositar(self, quantidade):
		self.saldo = self.saldo + quantidade

	def sacar(self, quantidade):
		if self.saldo >= quantidade:
			self.saldo = self.saldo - quantidade
			return self.saldo

	def calcular_rendimento(self, meses):
		return self.saldo * self.rendimento * meses

class ContaPoupanca(ContaBancaria):

	def __init__(self):
		super().__init__()
		self.rendimento = 0.02

class ContaCorrente(ContaBancaria):

	def __init__(self):
		super().__init__()
		self.rendimento = 0

class TesouroDireto(ContaBancaria):
	
	def __init__(self):
		super().__init__()
		self.rendimento = 0.1

	def sacar(self, quantidade):
		quantidade = quantidade * 1.03
		return super().sacar(quantidade)



if __name__ == '__main__':

	conta_bancaria = TesouroDireto()

	conta_bancaria.depositar(10)
	conta_bancaria.sacar(5)

	rendimento = conta_bancaria.calcular_rendimento(12)
	print('Meu rendimento será de: {}'.format(rendimento))

	saldo = conta_bancaria.saldo
	print('Meu saldo é de: {}'.format(saldo))