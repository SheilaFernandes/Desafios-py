from random import sample
from time import sleep
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
         30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60]
print('\033[1;33m-' * 45)
print(f'{"JOGO DA MEGA SENA":^45}')
print('-' * 45)
c = int(input('\033[1;34mQuantos jogos vocês quer que eu sortei? '))
for c in range(0, c):
    n = sorted(sample(lista, 6))
    print(f'Jogo {c+1}:', n)
    sleep(1)
print(f'\033[1;36m{"Boa Sorte":-^45}')
