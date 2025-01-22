pessoas = {}
dados = []
soma = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('nome: '))
    pessoas['idade'] = int(input('idade: '))
    soma += pessoas['idade']
    pessoas['sexo'] = str(input('sexo [M OU F]: '))
    dados.append(pessoas.copy())
    resp = str(input('Deseja parar?[S/N]: '))
    if resp  in 'Ss':
        break
print(f'{len(dados)} pessoas cadastradas')
media = soma / len(dados)
print(media)
print(f'as mulheres foram: ', end = ' ')
for pessoas in dados:
    if pessoas['sexo'] in 'Ff':
        print(f'{pessoas['nome']}')
print('acima da media:')
for pessoas in dados:
    if pessoas['idade'] >= media:
        print('    ')
        for k, v in pessoas.items():
            print(f'{k} = {v}')


