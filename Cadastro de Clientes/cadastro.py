import hashlib
import string
import random
from Classe_usuario import Usuario

def Cadastro():
	
	
	a = input("┌[Qual seu email? (back para sair)]:\n└──>")
	if a == 'back':
		return False
			
	b = input("┌[Digite sua senha]\n└──>")
	i = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
	
	i = bytes(i, encoding='utf8')
	b =	bytes(b, encoding='utf8')	
	b = hashlib.sha512(b + i).hexdigest()
	i = str(i)
	b = str(b)

	user = Usuario(a, b, i)
	user.register()


if __name__ == "__main__":

	Cadastro()
