a = int(input('Digite um número >>> '))
b = int(input('Digite outro número >>> '))
c = int(input('Digite mais um número >>> '))
d = int(input('Digite o ulimo número >>> '))
cont9 = cont3 = 0
tupla = (a, b, c, d)
lista = []

print(tupla)
'''if tupla[0] == 9:
    cont9 += 1
    print(cont9)
else:
    print('ok')
print(tupla[1] == 0)'''
for y in range(0, len(tupla)):
    if tupla[y] == 9:
        cont9 += 1
    if tupla[y] == 3:
        cont3 = y + 1
    if tupla[y] % 2 == 0:
        lista.append(tupla[y])
print(f'Você digitou os números {tupla}')
print(f'O número 9 apareceu {cont9} vezes')
if cont3 == 0:
    print(f'O número 3 não apareceu em nenhuma posição')
else:
    print(f'O número 3 apareceu na {cont3} posição:')
print(f'Os valores pares digitados foram {lista[0:]}')


