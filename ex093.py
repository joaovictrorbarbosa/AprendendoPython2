# FUNÇÃO LEIA INT
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok  = True
        else:
            print('\033[0;31mERRO. digite um numero inteiro.\033[m')
        if ok:
            break
    return valor

#PROGRAMA PRINCIPAL
n = leiaint('Digite um numero: ')
print(f'voce digitou o numero {n}')