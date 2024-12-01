nota1 = float(input('Digite aqui sua primeira nota: '))
nota2 = float(input('Digite aqui sua segunda nota: '))
media = (nota1 + nota2)/2

if media < 5.0:
    print('REPROVADO')
elif media >=5.0 and media < 7.0:
    print('RECUPERAÇÃO')
elif media > 7.0:
    print('APROVADO')