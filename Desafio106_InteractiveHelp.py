def anuncio():
    print('\033[1;46m~' * 45)
    print(f'{"SISTEMA DE AJUDA PyHELP":^45}')
    print('~' * 45, '\n\033[m')

def acessando():
    print('\033[1;45m~' * 70)
    print(f'{"Acessando o manual do comando ":^70} "`"{funçao}"`"')
    print('~' * 70, '\n\033[m')

def fechar():
    print('\033[1;41m~' * 20)
    print(f'{"Até logo":^20}')
    print('~' * 20, '\n\033[m')

def ajuda(a):
    from time import sleep
    acessando()
    sleep(0.5)
    print(f'\033[1;7m')
    {help(a)}
    print(f'\033[m')

#Programa Pincipal
while True:
    anuncio()
    funçao = input('Função ou Biblioteca >>> ')
    if funçao not in 'fimFIM':
        ajuda(funçao)
    else:
        break
fechar()
