import random
a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ')
n = random.choice([a, b, c, d])
print('{} '.format(n))

x = input('Primeiro Aluno: ')
y = input('Segundo Aluno: ')
z = input('Terceiro Aluno: ')
w = input('Quarto Aluno: ')
lista = [x, y, z, w]
escolhido = random.choice(lista)
print('{}'.format(escolhido))
#Um professo quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
#ele lendo os nomes deles e escrevendo o nome do escolhido