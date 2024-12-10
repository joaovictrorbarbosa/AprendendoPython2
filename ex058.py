n = cont = s = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma foi de {s}')
print(f'Foram digitados {cont} numeros')