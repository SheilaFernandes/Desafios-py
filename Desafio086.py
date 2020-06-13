matriz = [[], [], []]
for c in range(0, 3):
    matriz[c].append(int(input(f'Digite um valor para [{c}, 0]: ')))
    matriz[c].append(int(input(f'Digite um valor para [{c}, 1]: ')))
    matriz[c].append(int(input(f'Digite um valor para [{c}, 2]: ')))
print('-' * 20)
for v in matriz:
    print(f'\033[1;33m[{v[0]:^6}] [{v[1]:^6}] [{v[2]:^6}]')

