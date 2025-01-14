listanum = list()

while True:
    n = int(input('Digite um numero: '))
    if n not in listanum:
        listanum.append(n)
        print('VALOR ADICIONADO A LISTA.')
    else:
        print('VALOR DUPLICADO, NÃO ADICIONO.')
    r = str(input('QUER CONTINUAR DIGITANDO?[S/N]: '))
    if r in 'Nn':
        break
print('=-=-'*30)
listanum.sort()
print(listanum)
