from math import factorial
n = int(input('Digite um número para calcular seu fatorial >>> '))
f = factorial(n)
c = n
print('{}!= '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print('= ', end='')
    c -= 1
print('{}.'.format(f))
