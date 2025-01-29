#Função Voto
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return  f'Com idade de {idade} anos, o voto é PROIBIDO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com idade de {idade} anos, o voto é OPCIONAL'
    else:
        return f'Com idade de {idade} anos, o voto é OBRIGATORIO.'


#Programa principal
nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))