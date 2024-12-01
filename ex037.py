from datetime import date


print('CLASSIFICANDO CATEGORIA DE ATLETAS POR IDADE')
print('='*50)

atual = date.today().year
nascimento = int(input('EM QUE ANO O ATLETA NASCEU: '))
idade = atual - nascimento

print('O ATLETA É DA SEGUINTE CATEGORIA:')
if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <=25:
    print('SENIOR')
elif idade > 25:
    print('MASTER')

