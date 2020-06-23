def anuncio(msg):
    print('\033[1;46m~' * (len(msg)+4))
    print(f'  {msg}  ')
    print('~' * (len(msg)+4), '\n\033[m')

def acessando(msg2):
    print('\033[1;45m~' * (len(msg2) + 4))
    print(f'  {msg2}  : {funçao} ')
    print('~' * (len(msg2) + 4), '\n\033[m')

def fechar(msg2):
    print('\033[1;41m~' * (len(msg2) + 4))
    print(f'  {msg2}  ')
    print('~' * (len(msg2) + 4), '\n\033[m')

def ajuda(a):
    from time import sleep
    acessando("SISTEMA DE AJUDA PyHELP")
    sleep(0.5)
    print(f'\033[1;7m')
    {help(a)}
    print(f'\033[m')

#Programa Pincipal
while True:
    anuncio("SISTEMA DE AJUDA PyHELP",)
    funçao = str(input('Função ou Biblioteca >>> '))
    if funçao.upper() != 'FIM':
        ajuda(funçao)
    else:
        break
fechar("Até logo")
