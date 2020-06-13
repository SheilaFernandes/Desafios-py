num = int(input('digite um número de 0 a 9999: '))
print('Analisando o número {}'.format(num))
u = num //1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

