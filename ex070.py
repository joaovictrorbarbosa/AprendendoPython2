valores = list()
for c in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-=-'*30)
print(f'Voce digitou os valores: {valores}')
valores.sort()
print(f'O menor valor foi de {valores[0]}')
print(f'O maior valor foi de {valores[4]}')


