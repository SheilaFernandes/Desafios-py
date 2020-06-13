num = int(input('1º termo >>> '))
razao = int(input('Razão da PA >>> '))
a = 10
b = 10
ac = 10
c = 1
termo = num
while c <= 10:
    print('{} '.format(termo), end='')
    c += 1
    termo += razao
print('Pausa ...')
mais = int(input('Mais qnto?'))
while mais != 0:
    b += mais
    while ac < b:
        print('{} '.format(termo), end='')
        ac += 1
        termo += razao
    mais = int(input('Mais quantos números você quer mostrar? '))
print('Você leu {} números.'.format(b))
