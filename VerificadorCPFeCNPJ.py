def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, "")
    return new_string


def Verificar_cpf(cpf):
    cpf_str = (cpf + ".")[:-1]
    erro = f"Seu CPF: {cpf_str} é INVALIDO!"
    validar = f"Seu CPF: {cpf_str} é VALIDO!"

    def chr_remove(old, to_remove):
        new_string = old
        for x in to_remove:
            new_string = new_string.replace(x, "")
        return new_string

    cpf = chr_remove(cpf, ".- ,")
    error = cpf.isdigit()

    if error == False:
        print(erro)
        input("Enter to continue.")
        exit()
    cpf = [int(a) for a in str(cpf)]

    def calculo_cpf_1(cpf):
        index = 0
        valor = 10
        valor_cpf = []
        for i in cpf:
            if index <= 8:
                digito_cpf = cpf[index]
                valor_cpf_str = digito_cpf * valor
                valor_cpf.append(valor_cpf_str)
                index = index + 1
                valor = valor - 1
            else:
                break
        return valor_cpf

    valor_cpf = calculo_cpf_1(cpf)
    d = 0

    for i in valor_cpf:
        d = d + i
    calcular_cpf = list(cpf)
    comparar_cpf = list(cpf)
    d2 = int(d % 11)
    l = len(calcular_cpf)

    for numero in range(2):
        l = l - 1
        del calcular_cpf[l]

    if d2 >= 2:
        primeiro_digito_verificador = 11 - d2
        calcular_cpf.append(primeiro_digito_verificador)

    elif d2 < 2:
        calcular_cpf.append(0)
    index = 0
    valor = 11
    valor_cpf = []

    for i in calcular_cpf:
        if index <= 9:
            digito_cpf = calcular_cpf[index]
            valor_cpf_str = digito_cpf * valor
            valor_cpf.append(valor_cpf_str)
            index = index + 1
            valor = valor - 1

        else:
            break
    f = 0

    for i in valor_cpf:
        i = int(i)
        f = f + i

    definitivo = f % 11
    teste = definitivo < 2

    if teste == True:
        calcular_cpf.append(0)

    elif teste != True:
        f1 = 11 - definitivo
        calcular_cpf.append(f1)

    if calcular_cpf == comparar_cpf:
        print(validar)

    else:
        print(erro)


def Calcular_cnpj(cpf):
    cpf_str = (cpf + ".")[:-1]

    def chr_remove(old, to_remove):
        new_string = old
        for x in to_remove:
            new_string = new_string.replace(x, "")
        return new_string

    cnpj = chr_remove(cpf, ".- /,")
    error = cnpj.isdigit()
    erro = f"Seu CNPJ: {cpf_str} é INVALIDO!"
    validar = f"Seu CNPJ: {cpf_str} é VALIDO!"
    if error == False:
        print(error)
        input("Enter to continue.")
        exit()
    cnpj = [int(a) for a in str(cnpj)]

    def calculo_cnpj_1(cnpj):
        index = 0
        valor = 5
        valor_cnpj = []
        for i in cnpj:
            if valor == 1:
                valor = 9

            if index <= 11:
                digito_cnpj = cnpj[index]
                valor_cnpj_str = digito_cnpj * valor
                valor_cnpj.append(valor_cnpj_str)
                index = index + 1
                valor = valor - 1
            else:
                break
        return valor_cnpj

    valor_cnpj = calculo_cnpj_1(cnpj)
    d = 0
    for i in valor_cnpj:
        d = d + i
    calcular_cnpj_str = list(cnpj)
    comparar_cnpj = list(cnpj)
    d2 = int(d % 11)
    l = len(calcular_cnpj_str)

    for numero in range(2):
        l = l - 1
        del calcular_cnpj_str[l]

    if d2 >= 2:
        primeiro_digito_verificador = 11 - d2
        calcular_cnpj_str.append(primeiro_digito_verificador)

    elif d2 < 2:
        calcular_cnpj_str.append(0)
    index = 0
    valor = 6
    valor_cnpj = []

    for i in calcular_cnpj_str:
        if valor == 1:
            valor = 9

        if index <= 12:
            digito_cnpj = calcular_cnpj_str[index]
            valor_cnpj_str = digito_cnpj * valor
            valor_cnpj.append(valor_cnpj_str)
            index = index + 1
            valor = valor - 1

        else:
            break
    f = 0

    for i in valor_cnpj:
        i = int(i)
        f = f + i

    definitivo = f % 11
    teste = definitivo < 2

    if teste == True:
        calcular_cnpj_str.append(0)

    elif teste != True:
        f1 = 11 - definitivo
        calcular_cnpj_str.append(f1)

    if calcular_cnpj_str == comparar_cnpj:
        print(validar)

    else:
        print(erro)


if __name__ == "__main__":
    j = 0
    while j == 0:
        cpf = str(input("Digite o CPF/CNPJ: "))
        definir = chr_remove(cpf, ".-, /")
        if len(definir) == 14:
            Calcular_cnpj(cpf)
        elif len(definir) == 11:
            Verificar_cpf(cpf)
        else:
            print(f"Seu CPF/CNPJ digitado '{cpf}' é INVALIDO!")
        print("----//----//----//----//----//----//----")
