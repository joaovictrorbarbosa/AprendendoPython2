from ex104.lib.interface import *
from time import sleep
while True:
    resposta = menu(['Cadastrar pessoas', 'Listar pessoas', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até mais')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
    sleep(2)