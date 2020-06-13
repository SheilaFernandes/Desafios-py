# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostro quantos dolares ele tem
#Considerar 1 dolar = R$ 3,27
n = float(input('Informe quanto dinheiro (R$) você tem na carteira: R$ '))
D = n/3.27
print('\nVocê tem US$ {:.2f}\n\n\n considerando que US$1 equivale a R$3.27'.format(D))