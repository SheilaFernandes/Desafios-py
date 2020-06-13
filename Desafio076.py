tupla = ('Lapis', 1.75, 'Leite', 3.50, 'Frango', 10.90, 'Borracha', 2, 'Caderno', 15.90,
         'Estojo', 25, 'Transferidor', 4.20, 'Mochila', 120.95)
print('\033[1;33m{:-^70}\033[m'.format('-'))
print('\033[1;36m{:^70}'.format('LISTAGEM DE PREÇOS'))
print('\033[1;33m{:-^70}'.format('-'))
for c in range(0, len(tupla)):
    if c % 2 == 0:
        a = tupla[c+1]
        print(f'\033[1;34m{tupla[c]:.<40}','R${:<3}'.format(''), f'{tupla[c+1]:.2f}')
print('{:-40}'.format(""))
print(tupla[0],type(tupla[0]))
print(tupla[0+1], type(tupla[1]))