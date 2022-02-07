
def Verificar(numero):
	definitivo = 0
	numero_index = int(numero)
	while numero_index != 0:
		resultado = numero % numero_index
		if resultado == 0:
			definitivo = definitivo + 1
		
		numero_index = numero_index - 1
	
	if definitivo > 2:
		primo = False
		return primo
	else:
		primo = True
		return primo

while True:
	lista_de_resultados = []
	lista_de_numeros = []
	numero_para_verificar = None
	while numero_para_verificar != '-1':
		numero_para_verificar = input('┌[Digite seu numero inteiro(-1 para continuar)]\n└──> ')
		if numero_para_verificar != '-1':
			lista_de_numeros.append(numero_para_verificar)

	for i in lista_de_numeros:
		i = int(i)
		resultado = Verificar(i)
		if resultado:
			print(f'{i} é um numero primo!')
		else:
			print(f'{i} não é um numero primo!')

		

