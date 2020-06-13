salario = float(input('Digite seu salário >>> R$ '))
if salario > 1250.00:
    print('Seu salário terá aumento de 10%.\nSeu novo salário é R$ {:.2f}'.format(salario * 1.10))
else:
    print('Seu salário terá um aumento de 15%.\nSeu novo salário é R$ {:.2f}'.format(salario * 1.15))
print('Parabéns pelo seu aumento!!!')