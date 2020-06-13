# desenvolva um programa que leia a as duas notas de um aluno, calcule e mostre a sua média
a = float(input('Digite sua 1ª nota: '))
b = float(input('digite sua 2ª nota: '))
m = (a+b)/2
print('A média das notas que você informou é: {:>^20}.'.format(m))
