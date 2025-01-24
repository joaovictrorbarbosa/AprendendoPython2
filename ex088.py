from time import sleep

def  maior(*num):
    cont = maior = 0
    print('\nanalisando os valores...')
    sleep(1.0)
    for valor in num:
        print(f'{valor}', end = ' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram digitados {cont} valores')
    print(f'o maior foi {maior}')




#parte principal
maior (2,9,0,8,5,1)
maior(1,0)
maior(2,9,5)
maior()