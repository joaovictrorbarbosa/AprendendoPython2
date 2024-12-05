sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('DIGITE NOVAMENTE CORRETAMENTE SEU SEXO: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))
