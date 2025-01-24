from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando os numeros da lista:', end= ' ')
    sleep(0.5)
    for cont in range (0,5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('pronto.')

def somaPar(lista):
    sleep(0.5)
    soma = 0
    for valor in lista:
        if valor % 2 ==0:
            soma += valor
    print(f'somando os valores pares de {lista}...')
    sleep(0.5)
    print(f'Temos a soma {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)
