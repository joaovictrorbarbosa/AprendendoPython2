lista1 = []
lista2 = []
lista3 = []
while True:
    n = int(input('Digite um valor: '))
    lista1.append(n)
    if n % 2 == 0:
        lista2.append(n)
    elif n % 2 != 0:
        lista3.append(n)
    r = str(input('QUER CONTINUAR? [S/N]'))
    if r in 'Nn':
        break
print(f'Esses foram todos os numeros digitados: {lista1}')
print(f'Esses foram os numeros pares digitados: {lista2}')
print(f'Esses foram os numeros impares digitados: {lista3}')
