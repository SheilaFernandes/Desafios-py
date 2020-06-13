import random
a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ')
lista = [a, b, c, d]
random.shuffle(lista)
print('{}'.format(lista))

#O mesmo professo do desafio anterior quer sortear a ordem de apresentação de trabalho dos
# #alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.