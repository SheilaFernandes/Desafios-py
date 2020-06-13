import math
a = float(input('Digite um angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('o sen de {:.1f}º é >>> {:.2f}'.format(a, s))
print('o cos de {:.1f}º é >>> {:.2f}'.format(a, c))
print('a tan de {:.1f}º é >>> {:.2f}'.format(a, t))
#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo


