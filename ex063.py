print('=='*50)
print('''BANCO BARBOSA
SAQUES E DEPOSITOS APENAS.
DISPONIVEIS APENAS NOTAS DE R$1, R$10, R$20 E R$50.''')
print('=='*50)

valor = int(input('QUAL VALOR DESEJA SACAR: R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas  de R${ced}.')
        if ced == 50:
            ced =20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('OBRIGADO POR CONTAR CONOSCO.')