jogadores = list()
jogador = dict()
partidas = list()
soma = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, n):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
        soma += partidas[c]
    jogador['gols'] = partidas[:]
    jogador['total'] = soma
    jogadores.append(jogador.copy())
    partidas.clear()
    soma = 0
    while True:
        op = str(input('Quer Continuar [S/N]? ')).strip()[0]
        if op not in 'SsNn':
            print('Por favor digite S ou N.')
        else:
            break
    if op in 'Nn':
        break
print('\033[1;33m-' * 50)
print('cod ', end='')
for g in jogador.keys():
    print(f'{g:<30}', end='')
print()
for i, v in enumerate(jogadores):
    print(f'{i:<4}', end='')
    for k in v.values():
        print(f'{str(k):<30}', end='')
    print()
print('-' * 50)
while True:
    resp = int(input('\033[1;36mMostrar dados de qual jogador [999 encerra]?  \033[m'))
    if 0 < resp > (len(jogadores) - 1) and resp != 999:
        print(f'ERRO! Não existe jogador com código {resp}! Tente novamente. ')
    elif resp == 999:
        break
    else:
        print(f'----LEVANTAMENTO DO JOGADOR {jogadores[resp]["nome"]}: ')
        for x, h in enumerate(jogadores[resp]['gols']):
            print(f'   No jogo {x+1} fez {h} gols.')
        print('-' * 50)
print('<<VOLTE SEMPRE!!!>>')
