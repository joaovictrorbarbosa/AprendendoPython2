valor = float(input('QUAL O VALOR DO PRODUTO? R$ '))
parcelamento= int(input('O VALOR SERÁ PARCELADO? \n SE SIM, EM QUANTAS PARCELAS? \n caso não vá dividir, digite 1.\nnumero de parcelas: '))


avista = valor - (valor*10/100)
cartao = valor - (valor*5/100)
dividido2 = valor
dividido3 = int(valor + (valor*20/100))
parcela1 = valor/2
parcela2 = int(dividido3/parcelamento)

print('''QUAL SERÁ A OPÇÃO DE PAGAMENTO? 
1 - A VISTA
2 - CARTAO A VISTA
3 - DIVIDIDO EM ATE 2X
4 - DIVIDIDO EM 3X OU MAIS''')

opcao = int(input('ESCOLHA UMA OPÇÃO: '))

if opcao == 1:
    print('O VALOR DO PRODUTO SERÁ DE R${}'.format(avista))
elif opcao == 2:
    print('O VALOR DO PRODUTO SERÁ DE R${}'.format(cartao))
elif opcao == 3:
    print('O VALOR DO PRODUTO SERA DE R${}, COM PARCELAS DE R${}'.format(dividido2, parcela1))
elif opcao == 4:
    print('O VALOR DO PRODUTO SERÁ DE R${}, COM PARCELAS DE R${}'.format(dividido3, parcela2))
else:
    print('OPÇÃO INVALIDA.')