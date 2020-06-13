lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    if len(lista) == 1:
        print('Valor adicionado com sucesso ... ')
    elif lista.count(lista[-1]) == 1:
        print('Valor adicionado com sucesso ... ')
    else:
        print('Valor Duplicado! Não vou adicionar ... ')
        lista.pop()
    perg = input('Quer continuar: [S/N]: ').strip().upper()[0]
    if 'N' in perg:
        break
    while perg not in 'NSns':
        perg = input('Quer continuar: [S/N] ').strip().upper()[0]
lista.sort()
print(f'Você digitou  os valores {lista}')
