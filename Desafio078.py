valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
for p, count in enumerate(valores):
    if p != 0:
        if maior < count:
            maior = count
        else:
            maior = maior
        if menor > count:
            menor = count
        else:
            menor = menor
    else:
        maior = menor = count
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for v, g in enumerate(valores):
    if g == maior:
        print(f'{v}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for posi, m in enumerate(valores):
    if m == menor:
        print(f'{posi}...', end='')
