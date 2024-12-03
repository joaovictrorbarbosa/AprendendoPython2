maior = 0
menor = 0
for pessoas in range (1,6):
    peso = float(input('DIGITE QUAL SEU PESO EM KG: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR PESO EM KG FOI DE {}KG.'.format(maior))
print('O MENOR PESO EM KG FOI DE {}KG.'.format(menor))

