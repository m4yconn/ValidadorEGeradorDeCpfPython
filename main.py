from functions import *

menu = '''1 - validar CPF
2 - gerar um CPF
3 - sair do programa
Escolha a opção: '''

while True:

    while True:
        print()
        escolha = input(menu)
        
        if(escolha not in '123'):
            print("Opção inválida!\n")
            continue

        break

    if escolha == '1':

        while True:

            print()
            cpf = input("Digite um cpf (somente números): ")

            if cpf.isnumeric() and len(cpf) == 11:
                break

            print("\nDigite um formato correto! Ex: XXXXXXXXXXX")

        if(validarCpf(cpf)):
            print(f"O cpf: {formatarCpf(cpf)} é válido! ")

        else:
            print(f"O cpf: {formatarCpf(cpf)} é inválido! ")
    
    elif escolha == '2':

        cpf = gerarCpf()
        print()
        print("Cpf gerado!")
        print(formatarCpf(cpf))

    else:
        break

print("\nPrograma Encerrado.")