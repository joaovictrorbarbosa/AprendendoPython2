ficha  = []
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('QUER CONTINUAR? S OU N: '))
    if resp in 'Nn':
        break
print('+='*50)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('+='*50)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('+='*50)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FIM')
        break
    if opc <= len(ficha):
        print(f'NOTAS DE {ficha[opc][0]} são {ficha[opc][1]}')