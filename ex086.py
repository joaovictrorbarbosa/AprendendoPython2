#função:
def escreva(msg):
    tam = len(msg) + 4
    print('='* tam)
    print(f'  {msg}')
    print('=' * tam)


#Programa principal:
escreva('Joao')
escreva('estou aprimorando python')