from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
af = 18 - idade
alistamentoatrasado = idade - 18

print('sua idade é de {} anos.'.format(idade))

if idade < 18:
    print('Você deve se alistar apenas daqui há: {} anos.'.format(af))
elif idade == 18:
    print('Você deve se alistar este ano. Compareça ao tiro de guerra de sua cidade.')
elif idade > 18:
    print('Você deveria ter se alistado há {} ano(s). Compareça a um cartório para regularizar sua pendencia.'.format(alistamentoatrasado))
