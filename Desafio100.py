from random import randint
from time import sleep
def sorteio():
    l = list()
    soma = 0
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        l.append(randint(1, 10))
        print(l[c], end=' ')
        sleep(0.3)
        if l[c] % 2 == 0:
            soma += l[c]
    print(f'.\nSomando os valores pares de {l}, temos {soma}')
sorteio()
