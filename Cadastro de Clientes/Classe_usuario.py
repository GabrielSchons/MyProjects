import os

class Usuario():
	def __init__(self, email, senha, salt):
		self.email = email
		self.senha = senha
		self.salt = salt

	def register(self):
		x = {'email': self.email, 'senha': self.senha, 'salt': self.salt}
	
		os.system(f'echo "{x}" >> BancodeDados\n')