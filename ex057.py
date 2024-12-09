resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('QUER CONTINUAR DIGITANDO? [S/N]: ')).upper().strip()[0]
media = soma / quant
print(' a media dos valores digitados foi de {}.'.format(media))
print('O maior valor foi de {} e o menor foi de {}.'.format(maior, menor))
print('ACABOU')