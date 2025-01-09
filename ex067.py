num = (int(input('Digite um numero de 0 a 10: ')),
       int(input('Digite um numero de 0 a 10: ')),
       int(input('Digite um numero de 0 a 10: ')),
       int(input('Digite um numero de 0 a 10: ')),)
print(f'Voce digitou os seguintes numeros: {num}')
print(f'O numero 9  apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 foi digitado na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
print('Os valores pares digitados foram ', end= ' ')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')


