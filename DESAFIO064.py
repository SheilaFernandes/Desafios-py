n = int(input('Digite um número inteiro >>> '))
c = soma =0
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número inteiro >>> '))
print('Você digitou {} numero(s)'.format(c, soma))