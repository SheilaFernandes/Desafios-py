from datetime import date
ano = int(input('\033[1mInforme o seu ano de nascimento >>> '))
d = date.today().year - ano
if d == 18:
    print('\033[1:33m Esta na hora de você se alistar no exército!!')
elif d < 18:
    print('\033[34m Ainda falta \033[4m{} anos\033[m\033[34m para você se alistar. Fique tranquilo!!'.format(18-d))
else:
    print('\033[1;31m Se você ainda não se alistou CORRE!!!! Vao te sentar o cacete no exercito\n kkkkk...\n NÃO TO ZUANDO!!!')
