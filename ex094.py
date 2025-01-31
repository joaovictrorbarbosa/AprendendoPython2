#FUNÇÃO NOTA
def notas(*n , sit = False):
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max (n)
    r ['menor'] = min(n)
    r ['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação da sala'] = 'BOA'
        elif r['media'] >= 5:
            r['situação da sala'] = 'RAZOAVEL'
        else:
            r['situação da sala'] = 'RUIM'
    return r

#PARTE PRINCIPAL
resp = notas (3, 5, 5.5, 9, 10, sit= True)
print(resp)