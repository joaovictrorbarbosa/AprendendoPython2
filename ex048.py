frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('TEMOS UM PALINDROMO')
else:
    print('NAO É UM PALINDROMO')