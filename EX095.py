c = ('\033[m',    # 0 - sem cor
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - VERDE
    '\033[0;30;43m', # 3 - AMARELO
    '\033[0;30;44m' # 4 - AZUL
    );

def ajuda(com):
    help(com)

def titulo(msg, cor = 0):
    tam = len(msg) + 3
    print(c[cor], end ='')
    print('~' * tam)
    print(f' {msg}  ')
    print('~' * tam)
    print(c[0], end='')


#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca do Python --> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('FIM, ATE MAIS.', 1)