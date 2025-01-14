listan = []

while True:
    n = int(input('Digite um valor: '))
    listan.append(n)
    r = str(input('QUER CONTINUAR? [S/N]'))
    if r in 'Nn':
        break
print(f'Foram digitados {len(listan)} valores')
listan.sort()
print(f'Os valores digitados foram: {listan}')
if 5 in listan:
    print('Sim, o valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado')
