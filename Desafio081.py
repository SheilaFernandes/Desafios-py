valores = list()
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    p = str((input('Quer continuar? [S/N] '))).strip().upper()[0]
    while p not in 'NS':
        p = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if p == 'N':
        break
valores.sort(reverse=True)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem descrescente são {valores}')
if valores.count(5) == 0:
    print('O valor 5 nao faz parte da lista!')
else:
    print('O valor 5 faz parte da lista!')
