from datetime import date
a = int(input('Informe o ano de nascimento >>> '))
i = date.today().year - a
if i <= 9:
    print('Mirim')
elif i <= 14:
    print('Infantil')
elif i <= 19:
    print('Junior')
elif i <= 20:
    print('Sênior')
else:
    print('Master')
print('Sua idade é {}'.format(i))
