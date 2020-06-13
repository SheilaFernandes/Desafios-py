n = int(input('1º Termo: '))
r = int(input('Razão da PA: '))
t = int(input('Termo a ser identificado: '))
pa = n + (t - 1) * r
a = n
c = 2
print('{} '.format(n), end='')
while a < pa:
#while c <= t:
#while c <= 10:  -- neste caso delimita-se o número de termos em 10
    c += 1
    a += r
    print('{} '.format(a), end='')
