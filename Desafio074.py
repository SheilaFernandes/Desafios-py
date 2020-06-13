from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#d = (' ',' ', ' ', ' ', ' ',' ')
print(f'Os valores sorteados foram: ')
for pos, c in enumerate(lista):
    print(c, end=' ')
    if pos == 0:
        maior = menor = c
    else:
        if maior > c:
            maior = maior
        else:
            maior = c
        if menor < c:
            menor = menor
        else:
            menor = c
print('\033[1;31m\n',lista)
print(f'\033[1;36mO maior valor é {maior}')
print(f'O menor valor é {menor}')
print(f'\033[1;31mO maior valor é {max(lista)}')
print(f'\033[1;31mO menor valor {min(lista)}')
