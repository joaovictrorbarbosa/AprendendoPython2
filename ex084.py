jogador = {}
partidas =  []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input('quantas partidas o jogador jogou? '))
    partidas. clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols ele fez nesta partida {c+1}? ' )))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('DESEJA INCLUIR OUTRO JOGADOR?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
            break
print('cod',  end= ' ')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print( )
print('---'* 30)
for k, v in enumerate(time):
        print(f'{k:>3}', end= ' ')
        for d in v.values():
            print(f'{str(d): <15}', end= '  ')
        print()
print('---'* 30)
while True:
    busca = int(input('ESCOLHA QUAL JOGADOR, GOSTARIA DE VER DADOS ESPECIFICOS: [999 PARA ENCERRAR O PROGRAMA] '))
    if busca == 999:
        print('ENCERRANDO...')
        break
    if busca >= len(time):
        print(f'erro, nao temos jogadores com o codigo {[busca]}')
    else:
        print(f'Dados do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'Na partida {i+1}, fez {g} gols')
print('---'* 30)
