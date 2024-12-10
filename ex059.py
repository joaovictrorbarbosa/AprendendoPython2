while True:
    n = int(input('digite o numero que deseja saber a tabuada: '))
    if n < 0:
        break
    print('='*50)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    if n < 0:
        break
    print('=' * 50)
print('PROGRAMA ENCERRADO')
