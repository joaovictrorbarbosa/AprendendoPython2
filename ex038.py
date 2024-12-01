print('CALCULE SEU IMC')

altura = float(input('DIGITE SUA ALTURA (m): '))
peso = float(input('DIGITE SUA MASSA CORPORAL (Kg): '))
imc = (peso/altura**2)

print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc >=25.1 and imc <= 30:
    print('SOBREPESO')
elif imc >= 30.1 and imc <= 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MORBIDA')