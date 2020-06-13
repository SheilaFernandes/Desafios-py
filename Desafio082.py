numeros = []
pares = []
impares = []
c = 0
while True:
    numeros.append(int(input('Digite um valor>>> ')))
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
    c += 1
    p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while p not in 'NS':
        p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if p in 'N':
        break
print(f'A lista completa é {numeros}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números impares é {impares}')
