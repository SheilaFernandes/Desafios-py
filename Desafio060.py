'''n = int(input('digite um número '))
r = n
a = str('{}'.format(n))
for c in range(n -1, 0, -1):
    r = c * r
    a = str(a + ' x {}'.format(c))
print('{}!= {} = \033[1m{}'.format(n, a, r))'''
num = int(input('Digite um número inteiro>>> '))
c = num
f = 1
print('Calculando {}!= '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    f *= c
    c -= 1
    if c >= 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print('{}.'.format(f))
