from ex104.lib.interface import *
from ex104.lib.arquivo import *
from time import sleep

arq = 'barbosa.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar pessoas', 'Listar pessoas', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar conteudo de arquivo:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até mais')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
    sleep(2)