from random import randint
from time import sleep
from operator import itemgetter
jogada = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
          'Jogadro 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
ranking = list()
for k, c in jogada.items():
    print(f'\033[1;36mO {k} tirou {c} no dado')
    sleep(0.5)
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print(f'\033[1;33m{"Ranking dos Jogadores":-^30}')
for p, v in enumerate(ranking):
    print(f'\033[1;34m{p+1}º Lugar: {v[0]} tirou {v[1]}')
    sleep(0.5)
print(f'\033[1;33m{"Acabou":-^30}')

print(ranking)
a = {'idade': 5, 'peso': 10}
LISTA = list()
LISTA = sorted(a.items(), key=itemgetter(0))
print(LISTA)

