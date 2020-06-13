numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('digite um numero entre 0 e 20 >>> '))
        if 0 <= n <= 20:
            break
    print(f'\033[1;36mVocê digitou o número {numero[n]}')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer escolher outro número? [S/N]\033[m')).strip().upper()[0]
    if op == 'N':
        break
print('FIM')
