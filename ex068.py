listaproduto = ('lapis', 1.25,
                'caneta', 0.50,
                'borracha', 1.00,
                'caderno', 12.95)
print('-='*20)
print(f'{"LISTA DE PRODUTOS E PREÇOS":^40}')
print('-='*20)
for pos in range(0, len(listaproduto)):
    if pos % 2 == 0:
        print(f'{listaproduto[pos]:.<30}', end= '')
    else:
        print(f'R$ {listaproduto[pos]:>7.2f}')

