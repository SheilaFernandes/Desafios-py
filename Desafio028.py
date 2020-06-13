from random import randint
from time import sleep
import colorsys
n = randint(0, 5) #faz o computador "pensar".
#print(colorsys.rgb_to_yiq(r, g, b))
print('-=-' * 40)
print('Vou pensar em um número entre 0 e 5 ... Tente advinhar...')
print('-=-' * 40)
a = int(input('Qual número você acha que eu pensei? ')) #jogador digita qu
print('Processando...')
sleep(3)
if a == n:
    print('Você acertou... Parabéns!!')
else:
    print('Você errou!!!Eu pensei no número {}'.format(n))
