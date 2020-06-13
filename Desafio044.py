import random, time
lista = ('pedra', 'papel', 'tesoura')
a = random.randint(0, 2)
print('\033[1;35m++' * 35)
print('\033[1m Vamos jogar \033[1;31m Jokenpô\033[m !!!')
print('[0] PEDRA\n'
        '[1] PAPEL\n'
        '[2] TESOURA\n')
b = int(input('Escolha uma das opções acima: '))
if b != 0 and b != 1 and b != 2:
    print('JOGADA INVÁLIDA')
else:
    print('\033[1m Atenção...')
    print('Jo..')
    time.sleep(1)
    print('Ken..')
    time.sleep(1)
    print('pô..')
    print('\033[1;33m==' * 25)
    print('Você jogou: {}'.format((lista[b])))
    print('Eu joguei: {}'.format((lista[a])))
    print('\033[1;33m=='*25)
    if a == 0:
        if b == 1:
            print('\033[1;34m PARABENS!!! Você ganhou...')
        elif b == 2:
            print('GANHEI ... KKKK')
        elif b == 0:
            print('Empate ... vamos jogar denovo!')
    elif a == 1:
        if b == 0:
            print('GANHEI .... KKKK')
        elif b == 2:
            print('\033[1;34m PARABÉNS!!! Você ganhou ...')
        elif b == 1:
            print('Empate ... Vamos jogar denovo')
    elif a == 2:
        if b == 0:
            print('\033[1;34m PARABENS!!! Você ganhou ...')
        elif b == 1:
            print('GANHEI ... KKKK')
        elif b == 2:
            print('Empate ... Vamos jogar denovo')
