exp = input('Digite uma expressão >>> ').strip()
pa = []
for c in exp:
    if c == '(' or c == ')':
        pa.append(c)
    if c == ')':
        if '(' in pa:
            pa.pop()
            pa.pop()
if len(pa) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão esta errada')

