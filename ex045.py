soma = 0
cont = 0
for c in range(1,7):
    num = int(input('DIGITE O {}º NUMERO: '.format(c)))
    if num % 2 == 0:
        soma +=  num
        cont +=  1
print('A SOMA DOS NUMEROS É: {}'.format(soma, cont))


