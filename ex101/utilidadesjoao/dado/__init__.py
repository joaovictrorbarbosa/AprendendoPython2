#FUNÇÕES

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO \"{entrada}\" É  PREÇO INVALIDO\033[m')
        else:
            valido = True
            return float(entrada)

