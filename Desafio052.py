n = int(input('Digite um número inteiro >>> '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if cont == 2:
    print('\n\033[1;34mO número {} é número primo.'.format(n))
else:
    print('\n\033[1;34mO número {} não é número primo.'.format(n))
#print('\033[1;34m', c, end='-')
#print(cont)
