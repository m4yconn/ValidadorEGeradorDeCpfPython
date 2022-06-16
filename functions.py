from random import randint

def validarCpf(cpf):

    if cpf == (cpf[0] * 11): #Verificando se todos os digitos do cpf são iguais.
        return False
    
    penultimoDigito = verificaPenultimoDigito(cpf)
    ultimoDigito = verificaUltimoDigito(cpf)

    # print(penultimoDigito)
    # print(ultimoDigito)

    if ultimoDigito == int(cpf[-1]) and penultimoDigito == int(cpf[-2]):
        return True
    
    return False



def formatarCpf(cpf):
    cpf = list(cpf) #Trasnformando o cpf em uma lista para usar o metodo insert

    #Inserindo as pontuações do cpf
    cpf.insert(3, '.')
    cpf.insert(7, '.')
    cpf.insert(11, '-')

    cpf = ''.join(cpf)

    return cpf


def gerarCpf():

    cpf = randint(111111111, 999999999)
    cpf = str(cpf)

    penultimoDigito = verificaPenultimoDigito(cpf)
    cpf += str(penultimoDigito)

    ultimoDigito = verificaUltimoDigito(cpf)
    cpf += str(ultimoDigito)

    if not validarCpf(cpf):
        gerarCpf()

    else:
        return cpf



def verificaPenultimoDigito(cpf):
    penultimoDigito = 0

    for i in range(9):
        penultimoDigito += int(cpf[i]) * (10 - i)
    
    penultimoDigito = (penultimoDigito * 10) % 11
    if penultimoDigito > 9: penultimoDigito = 0

    return penultimoDigito


def verificaUltimoDigito(cpf):
    ultimoDigito = 0

    for i in range(10):
        ultimoDigito += int(cpf[i]) * (11 - i)

    ultimoDigito = (ultimoDigito * 10) % 11
    if ultimoDigito > 9: ultimoDigito = 0

    return ultimoDigito