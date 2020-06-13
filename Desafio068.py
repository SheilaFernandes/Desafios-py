from random import randint
print('\033[1;33m--'*20)
msg = 'VAMOS JOGAR PAR OU IMPAR!!!'
msgfinal = '\033[1;31mVocê Perdeu!!!\nG A M E  O V E R ! ! ! '
print(f'\033[1;34m{msg:^40}')
print('\033[1;33m--\033[m'*20)
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número inteiro: '))
    op = ' '
    while op not in 'PpIi':
        op = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    soma = jogador + computador
    if op == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} deu PAR.')
            print('--'*20)
            print('Você Venceu!')
            print('Vamos jogar novamente...')
            print(('--'*20))
            v += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} deu ÍMPAR.')
            break
    else:
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} deu ÍMPAR.')
            print('--'*20)
            print('Você Venceu!')
            print('Vamos jogar novamente...')
            v += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} deu PAR.')
            break
print('--'*20)
print(f'{msgfinal:^60}')
print(f'Você venceu {v} vezes')
