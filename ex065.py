times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco',
         'Vitoria', 'Atletico- MG', 'Fluminense', 'Gremio', 'Juventude',
         'Bragantino', 'Athletico', 'Criciuma', 'Atletico - GO', 'Cuiaba')
print('-='*30)
print(f'Lista de times: {times}')
print('-='*30)
print(f'Os 5 primeiros times são {times[:5]}')
print('-='*30)
print(f'Os 4 ultimos times são {times[16:]}')
print('-='*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*30)
print(f'O Corinthians está na {times.index('Corinthians')+1}ª posição.')
print('-='*30)
