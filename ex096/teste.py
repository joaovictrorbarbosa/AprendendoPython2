import moeda
p = float(input('Qual preço do produto? R$ '))
print(f'A metade do preço é de R${moeda.metade(p)}.')
print(f'O dobro do preço é de R${moeda.dobro(p)}.')
print(f'aumentando 20%, o valor será de R${moeda.aumentar(p,20)}.')
