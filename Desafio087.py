matriz = [[], [], []]
soma = soma3c = maior2l = 0
for c in range(0, 3):
    matriz[c].append(int(input(f'Digite um valor para [{c}, 0]: ')))
    matriz[c].append(int(input(f'Digite um valor para [{c}, 1]: ')))
    matriz[c].append(int(input(f'Digite um valor para [{c}, 2]: ')))
    soma3c += matriz[c][2]
    if matriz[c][0] % 2 == 0:
        soma += matriz[c][0]
    if matriz[c][1] % 2 == 0:
        soma += matriz[c][1]
    if matriz[c][2] % 2 == 0:
        soma += matriz[c][2]
    if c == 1:
        for p, z in enumerate(matriz[1]):
            if p == 0:
                maior2l = z
            elif matriz[1][p] > maior2l:
                maior2l = matriz[1][p]
print('\033[1;34m-' * 30)
for pos, v in enumerate(matriz):
    print(f'{v[0]:^6}{v[1]:^6}{v[2]:^6}')
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {maior2l}')
