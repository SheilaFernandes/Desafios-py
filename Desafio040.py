a = float(input('Informe sua 1ª nota >>> '))
b = float(input('Informe sua 2ª nota >>> '))
m = (a + b)/2
if m < 5:
    print('\033[1;31m REPROVADO')
elif m >= 5 and m <= 6.9:
    print('\033[;33m Recuperação')
else:
    print('\033[1;34m PARABENS!!! VOCÊ FOI APROVADO!!!!')
print('{}Sua média foi {}'.format('\033[1m', m))