prim = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
vigesimo = prim + (20-1) * razao
for c in range(prim , vigesimo , razao):
    print('{}'.format(c), end= '-')
print('FIM')