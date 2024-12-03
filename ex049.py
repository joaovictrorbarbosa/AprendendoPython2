from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,8):
    nasc = int(input('ANO DE NASCIMENTO: '.format(c)))
    idade = atual - nasc
    if idade < 18:
        totmaior+= 1
    else:
        totmenor+= 1
print('O TOTAL DE PESSOAS MAIORES É IGUAL A {}'.format(totmaior))
print('O TOTAL DE PESSOAS MENORES É IGUAL A {}'.format(totmenor))
