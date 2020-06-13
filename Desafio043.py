a = float(input('Qual a sua altura? '))
p = float(input('Qual seu peso?'))
i = (p / pow(a, 2))
if i <= 18.5:
    print('Abaixo do Peso')
elif i > 18.5 and i <= 25:
    print('Peso ideal')
elif i > 25 and i <= 30:
    print('Sobrepeso')
elif i > 30 and i <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
print('Seu IMC é {:.2f}'.format(i))
