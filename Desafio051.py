print('\033[1;33m='*35)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('\033[1;33m='*35)
p = int(input('Primeiro termo >>> '))
r = int(input('Razão >>> '))
"""p1 = p - r
for c in range(p, p + 10):
    p += r
    print(p, end='-')
print('\033[1;35mACABOU')"""
d = p + (10-1) * r
for c in range(p, d, r):
    print(c, end='-')
print('\033[1;35mACABOU')
