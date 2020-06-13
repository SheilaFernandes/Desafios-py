n = int(input('Digite um número inteiro >>> '))
print('\033[36m-'*15)
for c in range(0, 11):
    r = n * c
    print('\033[1;33m{} x {:2} = {}'.format(n, c, r))
print('\033[36m-'*15)
