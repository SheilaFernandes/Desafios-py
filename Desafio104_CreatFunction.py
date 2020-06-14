'''A função leiaInt() vai receber uma msg (linha 16) que o usario digitar'''
def leiaInt(msg):
    #variavel ok valida se o input do usuário é númerico (True) ou nao (False)
     ok = False
     valor = 0
     while True:
        #A variavel n vai receber o input da msg, ou seja, o número que o usuário digitou.
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[36;1m ERRO! Digite um numero inteiro válido.\033[m')
        if ok:
            break
     return valor
#Programa Principal
n = leiaInt('digite un número >>> ')
print(f'Você digitou o número {n}')



