from random import randint

computador = randint(0,10)
print('aqui é o seu PC, pensei um numero de 0 a 10')
print('Consegue adivinhar qual??')

jogador = int(input('Digite um numero: '))
tentativas = 0
while jogador != computador:
    jogador = int(input('Voce errou, digite outro valor: '))
    tentativas += 1
    if jogador == computador:
        print('VOCE ACERTOU PARABENS.')
        tentativas += 1
print('O numero de tentativas para acertar meu numero foi de {}'.format(tentativas))

