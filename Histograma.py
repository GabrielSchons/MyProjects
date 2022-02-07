def Histograma(lista):
	valor_anterior = 0
	for item in lista:
		valorzin = []
		metrica = []
		while item != 0:
			valorzin.append('▄ ')
			if item > valor_anterior:
				valor_anterior = item
			item -= 1
		print(''.join(map(str, valorzin)))

	while valor_anterior > 0:
		metrica.append(valor_anterior)
		valor_anterior -= 1
	print(' '.join(map(str, metrica[::-1])))

numeros = [
  3,
  9,
  7,
  4,
]
Histograma(numeros)
