from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou o numero {v} no dado.')
    sleep(2)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse= True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v}')
