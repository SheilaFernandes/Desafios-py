# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60/dia
# e R$0,15/km rodado;
d = float(input('Qual a quantidade km percorridos em km? '))
t = float(input('Qual a quantidade de dias que você ficou com o veículo alugado? '))
print('O Valor do aluguel é R${:.2f}'.format((d * 0.15 + t * 60)))