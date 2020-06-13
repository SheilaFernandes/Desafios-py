import math
a = float(input('Digite 1º número >>> '))
b = float(input('Digite 2º número >>> '))
c = float(input('Digite 3º número >>> '))
#Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))


#outra forma de fazer o código.
"""if a > b and a > c:
    print('Maior número é {}'.format(a))
if b > a and b > c:
    print('Maior número é {}'.format(b))
if c > a and c > b:
    print('Maior número é {}'.format(c))
print('--------FIM--------')"""