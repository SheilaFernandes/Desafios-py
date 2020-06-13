# Crie um algoritmo que leia o número e mostre o seu dobro, tripo e raiz quadrada
n = int(input("Digite um número: "))
d = n*2
t = n*3
R = pow(n,1/2)
print('O dobro do número {} é: {} \nO triplo do número {} é: {} \nE a raiz '
      'quadrada do número {} é: {:.3f}'.format(n, d, n, t, n, R))
