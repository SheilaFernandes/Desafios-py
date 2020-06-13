n = int(input('Digite um número inteiro >>> '))
cont = 1
soma = n
maior = n
menor = n
p = 'S'
p = str(input('Deseja digitar outro número? [S/N] ')).strip().upper()
while p == 'S':
    n = int(input('Digite um número inteiro >>> '))
    p = str(input('Deseja digitar outro número? [S/N] ')).strip().upper()
    cont += 1
    soma += n
    if maior < n:
        maior = n
    else:
        maior = maior
    if menor > n:
        menor = n
    else:
        menor = menor
media = soma/cont
if cont == 1:
    print('Não existe número maior nem menor. Você digitou apenas {} número.'.format(cont))
    print('A média é {}'.format(media))
else:
    print('você digitou {} numeros, maior {} menor {} e a média é {}'.format(cont, maior, menor, media))
