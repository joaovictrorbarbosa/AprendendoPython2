from ex104.lib.interface import *

def arqExiste(nome):
    try:
        a =open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'ARQUIVO {nome} CRIADO COM SUCESSO')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())