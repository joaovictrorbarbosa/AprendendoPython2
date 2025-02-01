from ex096 import moeda
print(moeda.resumo())
p = float(input('Qual preço do produto? R$ '))
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é de {moeda.dobro(p, True)}.')
print(f'aumentando 20%, o valor de {moeda.moeda(p)} será de {moeda.aumentar(p,20, True)}.')