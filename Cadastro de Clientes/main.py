from cadastro import Cadastro
from ler_banco_de_dados import Funcao_verificadora



def main():
	
	opcao = input("┌[Você quer CADASTRAR ou ACESSAR uma conta?]\n└──>").upper()

	if opcao == "CADASTRAR":
		Cadastro()
		main()
	elif opcao == "ACESSAR":
		verificador = Funcao_verificadora()
		if verificador == True:
			print('Seja bem vindo!')
		else:
			input('Conexão rejeitada, senha errada ou usuario não encontrado.\nEnter para continuar.')
		main()
	else:
		input(f'Opção "{opcao}" invalida, por favor, digite uma opção valida.')
		main()

if __name__ == "__main__":
	main()