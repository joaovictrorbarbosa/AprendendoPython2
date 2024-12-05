from time import sleep
num1 = int(input('DIGITE UM NUMERO: '))
num2 = int(input('DIGITE UM NUMERO: '))
opcao = 0
while opcao != 5:
    print('''MENU:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA''')

    opcao = int(input('DIGITE QUAL OPÇÃO DESEJA: '))

    if opcao == 1:
        print(num1+num2)
    elif opcao == 2:
        print(num1*num2)
    elif opcao == 3:
        if num1>num2:
            maior = num1
        else:
            maior = num2
        print('O maior numero é {}'.format(maior))
    elif opcao == 4:
        print('Informe os novos numeros:')
        num1 = int(input('DIGITE O PRIMEIRO NUMERO: '))
        num2 = int(input('DIGITE O SEGUNDO NUMERO: '))
    elif opcao == 5:
        sleep(0.5)
        print('Finalizando....')
    else:
        print('Opção Invalida.Tente novamente.')
print('='*30)
print('FIM DO PROGRAMA.')





