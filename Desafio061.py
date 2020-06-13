num = int(input('1º termo >>> '))
razao = int(input('Razão da PA >>> '))
pa = num + (10 - 1) * razao
termo = num
c = 2
print('{} '.format(termo), end='')
while c <= 10:
#while termo < pa: caso não quiser utilizar um contador pode
    termo += razao
    c += 1
    print('{} '.format(termo), end='')
