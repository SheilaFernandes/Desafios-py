a = int(input('\033[1;35m Digite um número inteiro >>> '))
b = int(input('\033[1;35m Digite outro número inteiro >>> '))
if a > b:
    print('\033[1;34m O PRIMEIRO número \033[4m({})\033[m \033[1;34mé o maior!'.format(a))
elif b > a:
    print('\033[1;34m O SEGUNDO número \033[4m({})\033[m \033[1;34mé o maior!'.format(b))
else:
    print ('\033[1;33mNão existe valor maior. Os dois são iguais!')
