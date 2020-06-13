lista = [[],[],[]]
n = 0
somapar = soma3c = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = lista[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        if lista[l][c] % 2 == 0:
            somapar += lista[l][c]
        if c == 2:
            soma3c += lista[l][c]
        if l == 1:
            if c == 0:
                maior = lista[l][c]
            elif lista[l][c] > maior:
                maior = lista[l][c]
        print(f'\033[1;34m[{lista[l][c]:^6}]', end=' ')
    print()
print(f'\033[1;33mA soma dos números pares é {somapar}')
print(f'A soma dos valores da 3ª coluna é {soma3c}')
print(f'O maior valor da 2ª linha é {maior}')
