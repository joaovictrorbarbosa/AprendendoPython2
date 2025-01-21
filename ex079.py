aluno = {}
aluno ['NOME'] = str(input('NOME: '))
aluno ['MÉDIA'] = float(input(f'MÉDIA DE {aluno["NOME"]}:  '))
if aluno['MÉDIA'] >= 7:
    aluno['SITUAÇÃO'] = 'Aprovado'
elif 5 <=  aluno['MÉDIA'] < 7:
    aluno['SITUAÇÃO'] = 'Recuperação'
else:
    aluno['SITUAÇÃO'] = 'REPROVADO'

for k, v in aluno.items():
    print(f' {k} --- {v}')