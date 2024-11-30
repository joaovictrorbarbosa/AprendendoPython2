num = int(input('Digite um numero qualquer: '))

print('Qual base de conversao gostaria que seu numero ficasse? \n 1-Binario \n 2-Octal \n 3-Hexadecimal')

base = int(input('Digite qual base será: '))
if base == 1:
    print('{} na base binaria é: {}'.format(num, bin(num)))
elif base == 2:
    print('{} na base octal será: {}'.format(num, oct(num)))
elif base == 3:
    print('{} na base hexadecimal será: {}'.format(num, hex(num)))
