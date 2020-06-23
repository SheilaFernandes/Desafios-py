def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido \033[m')
            continue #ele retorna para o while
        except (KeyboardInterrupt):
            #aqui nao funciona este comando mas nao VSCode funciona para caso o usuario interromper o programa
            print('Entrada de dadas interrompida pelo usuario')
            return 0
        else:
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[1;31mERRO! Digite um número real válido\033[m')
            continue
        else:
            return n


nInt = LeiaInt('Digite um número Inteiro ')
nReal = LeiaFloat('Digite um número real ')
print(f'O valor inteiro digitado é {nInt} e o valor real digitado é {nReal}')
