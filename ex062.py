somaprodutos = produtommil = menor = cont =  0
while True:
    nomeproduto = str(input('DIGITE O NOME DO PRODUTO: '))
    precoproduto = float(input('DIGITE O VALOR DO PRODUTO: R$'))
    cont += 1
    somaprodutos += precoproduto
    if precoproduto > 1000:
        produtommil +=1
    if cont == 1:
        menor = precoproduto
    else:
        if precoproduto < menor:
            menor = precoproduto
    resp = ' '
    while resp not in 'SN':
        resp = (input('GOSTARIA DE CONTINUAR COMPRANDO?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('='*50)
print(f'O valor total foi de R${somaprodutos}')
print(f'Foi registrado {produtommil} produto(s) acima de R$1000.')
print(f'O menor valor foi de R${menor}')
print('FIM DE COMPRA, VOLTE SEMPRE.')

