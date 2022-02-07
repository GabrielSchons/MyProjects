import hashlib

def Funcao_verificadora():
	def verificara(email, linha):
		certo = None
		with open('BancodeDados') as temp_f:
			datafile = temp_f.readlines()
		for line in datafile:
			if email in line[11:-163]:
				certo = True
				break		
			else:
				linha = linha + 1
				

		if email == '\n' or email == '' or email == ' ':
			return False, False

		elif certo:
			return linha, datafile

		return False, False
		

	while True:
	
		email = input("┌[qual seu Email?]\n└──>")
		tamanho_email = len(email)
		pular = 24 + tamanho_email
		linha = 1
	
		linha, datafile = verificara(email, linha)

		
		if linha == False:
			return False

		elif linha != False:
			senha = input("┌[qual sua senha?]\n└──>")

		verificar_senha = datafile[linha - 1][pular:-22]
		codigo_salt = datafile[linha - 1][164 + tamanho_email:-2]
		senha = bytes(senha, encoding='utf8')
		codigo_salt = bytes(codigo_salt, encoding='utf8')
		tentativa_de_login = hashlib.sha512(senha + codigo_salt).hexdigest()
		if verificar_senha == tentativa_de_login:
			return True
		else:
			return False

if __name__ == "__main__":
	while True:
		Funcao_verificadora()
