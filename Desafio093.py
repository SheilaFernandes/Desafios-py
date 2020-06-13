info = dict()
partidas = list()
tot = 0
info['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {info["nome"]} jogou? '))
for c in range(0, n):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
info['gols'] = partidas[:]
info['total'] = sum(partidas)
print('-' * 40)
for a, b in info.items():
    print(f'O campo {a} tem valor {b}.')
print('\033[1;33m*' * 40)
print(f'\033[1;36mO jogador {info["nome"]} jogou {n} partidas.')
for i in range(0, n):
    print(f'    =>Na partida {i+1}, fez {info["gols"][i]} gols. ')
print(f'Foi um total de {info["total"]} gols.')
print('\033[1;33m*' * 40)
print(info)
