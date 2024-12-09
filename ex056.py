n = c = soma = 0
while n != 999:
    n = int(input('Digite um numero [999 para o programa]: '))
    soma += n
    c +=1
print('voce digitou {} numeros e a soma entre eles foi de {}.'.format(c -1, soma -999))