while True:
	lista = []
	numero = None
	
	while numero != 'ok':
		numero = input('[Qual o numero? (ok para continuar)]-> ')
		if numero != 'ok':
			lista.append(numero)
	
	for i in lista:
		if int(i) % 2 == 0:
			print(f'o numero {i} é par!')
		else:
			print(f'o numero {i} é impar')
