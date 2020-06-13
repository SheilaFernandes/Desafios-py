# Faça um algoritmo que leia o preço de um produto e mostre novo preço com 5% de desconto.
p = float(input('Informe o preço do produto sem desconto >>> R$'))
n = p*0.95
print('O valor do produto com 5% de desconto é R${:.2f}.'.format(n))
