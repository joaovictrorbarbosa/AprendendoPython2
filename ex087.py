from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end =' ', flush= True)
            sleep (0.5)
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end = ' ', flush= True)
            sleep(0.5)
            cont -= p
        print('fim')

#Parte principal
contador(1, 10, 1)
contador(10, 0, 2)
print('ESCOLHA O INICIO, FIM E OS PASSOS')
ini = int(input('digite o inicio: '))
fim = int(input('digite o fim: '))
passo = int((input('digite os passos: ')))
contador(ini, fim, passo)