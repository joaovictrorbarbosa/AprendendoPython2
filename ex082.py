jogador = {}
partidas =  []
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input('quantas partidas o jogador jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols ele fez nesta partida {c+1}? ' )))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
for k, v in jogador.items():
    print(f'{k} : {v}')
