import os

def Menu(valor, tipo):
	def Oct_bin(valor):
		valor = Oct_dec(valor)
		valor = Dec_bin(valor)
		return valor

	def Bin_oct(valor):		
		valor = Bin_dec(valor)
		valor = Dec_oct(valor)
		return valor

	def Oct_hex(valor):
		valor = Oct_dec(valor)
		valor = Dec_hex(valor)
		return valor

	def Hex_oct(valor):
		valor = Hex_dec(valor)
		valor = Dec_oct(valor)
		return valor

	def Dec_oct(valor):
		numero = int(valor)
		valor = "%o" % numero
		return valor

	def Oct_dec(valor):
		numero = int(valor)
		num_oct = [str(a) for a in str(numero)]
		x = len(num_oct) - 1
		soma_final = []
		for l in num_oct:
			if l == "9" or l == "8":
				input("Não é um numero Octal.")
				os.system('cls' if os.name == 'nt' else 'clear')
				Inicio()

		for i in num_oct:
			i = int(i)
			multiplicador = 8 ** x
			e = i * multiplicador
			x = x - 1
			soma_final.append(int(e))
		valor = sum(soma_final)
		return valor

	def Dec_bin(valor):
		numero = int(valor)
		numero_bin = bin(numero)
		num_bin = [str(a) for a in str(numero_bin)]
		for X in range(2):
			del num_bin[0]
		valor = "".join(num_bin)
		return valor

	def Dec_hex(valor):
		valor = int(valor)
		valor = "%X" % valor
		return valor

	def Bin_dec(valor):
		numero = valor
		num_bin = [str(a) for a in str(numero)]
		for a in num_bin:
			if a != "0" and a != "1":
				input("Não é um numero binário.")
				os.system('cls' if os.name == 'nt' else 'clear')
				Inicio()
		x = len(num_bin) - 1
		soma_final = []
		for i in num_bin:
			i = int(i)
			multiplicador = 2 ** x
			e = i * multiplicador
			x = x - 1
			soma_final.append(int(e))
		valor = sum(soma_final)
		return valor

	def Hex_dec(valor):
		numero = valor
		num_hex = [str(a) for a in str(numero)]
		for index, value in enumerate(num_hex):
			if value.islower():
				value = value.upper()

			if value == "A":
				num_hex[index] = 10
			elif value == "B":
				num_hex[index] = 11
			elif value == "C":
				num_hex[index] = 12
			elif value == "D":
				num_hex[index] = 13
			elif value == "E":
				num_hex[index] = 14
			elif value == "F":
				num_hex[index] = 15

		x = len(num_hex)
		x = x - 1
		soma_final = []
		for i in num_hex:
			i = int(i)
			multiplicador = 16 ** x
			e = i * multiplicador
			x = x - 1
			soma_final.append(int(e))
		valor = sum(soma_final)
		return valor

	def Hex_bin(valor):
		valor_dec = Hex_dec(valor)
		valor = valor_dec
		valor = Dec_bin(valor)
		return valor

	def Bin_hex(valor):
		valor_bin = Bin_dec(valor)
		valor = valor_bin
		valor = Dec_hex(valor)
		return valor

	def Bin_all(valor):
		ver_bin = [int(x) for x in str(valor)]
		for i in ver_bin:
			if i > 1:
				input("Valor inválido!")
				os.system('cls' if os.name == 'nt' else 'clear')
				Inicio()
		print(f"Dec: {Bin_dec(valor)}\nBin: {valor}\nHex: {Bin_hex(valor)}\nOct: {Bin_oct(valor)} ")

	def Dec_all(valor):
		controle = type(valor)
		valor = str(valor)
		variavel = valor.isdigit()
		if variavel != True:
			input("Valor inválido!")
			os.system("clear")
			Inicio()
		valor = controle(valor)
		print(f"Dec: {valor}\nBin: {Dec_bin(valor)}\nHex: {Dec_hex(valor)}\nOct: {Dec_oct(valor)} ")
	
	def Hex_all(valor):
		valor = valor.upper()
		ver_hex = [str(x) for x in str(valor)]
		for i in ver_hex:
			if i != "A" and i != "B" and i != "C" and i != "D" and i != "E" and i != "F" and i.isdigit() != True:
				input("Não é um valor em Hexadecimal!")
				os.system('cls' if os.name == 'nt' else 'clear')
				Inicio()
				
		print(f"Dec: {Hex_dec(valor)}\nBin: {Hex_bin(valor)}\nHex: {valor}\nOct: {Hex_oct(valor)} ")

	def Oct_all(valor):
		if valor == 8 or valor == 9:
			input("Valor inválido!")
			Inicio()
		print(f"Dec: {Oct_dec(valor)}\nBin: {Oct_bin(valor)}\nHex: {Oct_hex(valor)}\nOct: {valor} ")	

	if tipo == "bin":
		while valor != "aaaaaaaaaaa":
			if valor != "back":
				Bin_all(valor)
				valor = input("Qual seu valor binário? (back para voltar)\n> ")
				print()
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
				Inicio()

	elif tipo == "dec":
		while valor != "aaaaaaaaaaa":
			if valor != "back":
				Dec_all(valor)
				valor = input("Qual seu valor decimal? (back para voltar)\n> ")
				print()
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
				Inicio()

	elif tipo == "hex":
		while valor != "aaaaaaaaaaaa":
			if valor != "back":
				Hex_all(valor)
				valor = input("Qual seu valor hexadecimal? (back para voltar)\n> ")
				print()
			else:
				os.system("clear")
				Inicio()

	elif tipo == "oct":
		while valor != "aaaaaaaaaaaa":
			if valor != "back":
				Oct_all(valor)	
				valor = input("Qual seu valor octal? (back para voltar)\n> ")
				print()
			else:
				os.system("clear")
				Inicio()

if __name__ == "__main__":
	def Inicio():
		l = 0
		while l == 0:

			tipo = input(f"Qual o tipo do seu valor?\ndec> decimal\nbin> binario\nhex> hexadecimal\noct> octal\n> ")
			print()
			valor = input("Qual seu valor?\n> ")
			print()
			tipo = tipo.casefold()
			if tipo == "back":
				Inicio()

			if tipo == "hexadecimal":
				tipo = "hex"
			elif tipo == "decimal":
				tipo = "dec"
			elif tipo == "binario":
				tipo = "bin"
			elif tipo == "octal":
				tipo = "oct"

			Menu(valor, tipo)

Inicio()
