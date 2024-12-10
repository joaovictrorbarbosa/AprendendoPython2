conti = conth = contm = 0
while True:
    idade = int(input('DIGITE SUA IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('QUAL SEU SEXO?[M/F]: ')).strip().upper()[0]
    if idade < 18:
        conti += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm +=1
    resp = ' '
    while resp not in 'SN':
        resp = (input('GOSTARIA DE CONTINUAR?[S/N]:  ').strip().upper())[0]
    if resp == 'N':
            break
print('acabou')
print(f'Existem {conti} pessoas com menos de 18 anos.')
print(f'Existem {conth} homens.')
print(f'Existem {contm} mulheres com menos de 20 anos.')