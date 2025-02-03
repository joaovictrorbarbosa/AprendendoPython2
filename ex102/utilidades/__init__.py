# FUNÇÃO LEIA INT
def leiaint(msg):
    valor = 0
    while True:
        try:
            n = int(input(msg))
            valor = int(n)
        except:
            print('\033[0;31mERRO. digite um numero inteiro.\033[m')
            continue
        else:
            return valor

def leiafloat(msg):
    valor = 0
    while True:
        try:
            n2 = float(input(msg))
            valor = float(n2)
        except:
            print('\033[0;31mERRO. digite um numero real.\033[m')
        else:
            return valor