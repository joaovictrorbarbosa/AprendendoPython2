from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''Suas Opções são:
0- Pedra
1- Papel
2  Tesoura''')
jogador = int(input('DIGITE SUA OPÇÃO? '))
print('O computador escolheu {}'.format(itens[computador]))
if jogador == 0 and computador == 1:
    print('COMPUTADOR GANHOU')
elif jogador == 1 and computador == 0:
    print('VOCE GANHOU')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR GANHOU')
elif jogador == 2 and computador == 1:
    print('VOCE GANHOU')
elif jogador == 0 and computador == 2:
    print('VOCE GANHOU')
elif jogador == 2 and computador == 0:
    print('COMPUTADOR GANHOU')
elif jogador == 0 and computador == 0:
    print('NINGUEM GANHOU')
elif jogador == 1 and computador == 1:
    print('NINGUEM GANHOU')
elif jogador == 2 and computador == 2:
    print('NINGUEM GANHOU')