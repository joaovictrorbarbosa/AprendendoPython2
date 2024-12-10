from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? ')).strip().upper()
    print(f'voce jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        if total % 2 != 0:
            print('VOCE PERDEU')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('VOCE VENCEU')
            v+=1
        if total % 2 ==0:
            print('VOCE PERDEU')
            break
    print('VAMOS JOGAR NOVAMENTE')
print(f'FIM DE JOGO: VOCE VENCEU {v} VEZES.')