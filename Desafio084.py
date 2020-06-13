lista = list()
dado = list()
pesadas = list()
leves = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while True:
        if perg in 'SN':
            break
        else:
            perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
for n, c in enumerate(lista):
    if n == 0:
        pesadas.append(c)
        leves.append(c)
    elif c[1] > pesadas[0][1]:
        pesadas.clear()
        pesadas.append(c)
    elif c[1] == pesadas[0][1]:
        pesadas.append(c)
    elif c[1] < leves[0][1]:
        leves.clear()
        leves.append(c)
    elif c[1] == leves[0][1]:
        leves.append(c)
print(f'Você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {pesadas[0][1]} Kg. Peso de: ', end='')
for p in pesadas:
    print(f'{p[0]},', end=' ')
print(f'\nO menor peso foi de {leves[0][1]} Kg. Peso de: ', end='')
for v in leves:
    print(f'{v[0]},', end=' ')
