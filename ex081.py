from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho [0 = não consta]: '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário (em R$): '))
    dados['Aposentadoria'] = dados['contratação'] + 35
else:
    print('Você ainda não trabalhou, ainda não pode calcular sua aposentadoria.')
for k, v in dados.items():
    print(f' - {k} tem o valor:  {v}')
