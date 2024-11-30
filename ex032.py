print('Aprovar Financiamento.')

casa = int(input('Qual o valor da casa? R$ '))
salario = int(input('Qual seu salario? R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))

prestacaomensal = (casa/anos)/12

if prestacaomensal > (salario*30)/100:
    print('Emprestimo negado, prestação maior que 30% de seu salario.')
else:
    print('Parabéns seu emprestimo foi aprovado, suas parcelas serão de R${:.2f}.'.format(prestacaomensal))


