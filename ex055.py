from math import factorial
n = int(input('DIGITE UM NUMERO PARA CALCULAR: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print('{}'.format(f))

