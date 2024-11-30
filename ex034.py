num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O numero {} é maior que o numero {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que o numero {}'.format(num2, num1))
elif num1 == num2:
    print('Não existe valor maior, pois os dois numeros são iguais!')
