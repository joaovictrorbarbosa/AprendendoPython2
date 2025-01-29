#FUNÇÃO FICHA
def ficha(jog= 'desconhecido', gol = 0):
    print(f'{jog} fez {gol} gols no campeonato.')


#PROGRAMA PRINCIPAL
n= str(input('Nome do Jogador: '))
g = str(input('Quantos gols ele fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)

