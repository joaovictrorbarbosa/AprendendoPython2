princ = []
par = []
impar = []

for n in range(0,7):
    n = int(input('DIGITE UM NUMERO: '))
    princ.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)

print(f'Os números digitados foram: {princ}.')
par.sort()
print(f'Os numeros pares digitados foram: {par}.')
impar.sort()
print(f'Os numeros pares digitados foram: {impar}.')

