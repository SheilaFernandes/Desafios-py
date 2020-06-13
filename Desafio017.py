from math import sqrt, hypot
cop = float(input('Informe o valor do cateto oposto: '))
cad = float(input('Informe o valor do cateto adjacente: '))
r = cop ** 2 + cad ** 2
h = sqrt(r)
print('O triangulo retângulo que possúi cateto oposto com medida de {:.2f} e cateto adjacente\n'
      'com medida de {:.2f}, apresenta hipotenusa com o comprimento de {:.2f}'.format(cop, cad, h))


#faça um progrma que leia o comprimento do cateto oposto do cateto adjcente de um triangulo realngulo. calcule
# e mostre o comprimento da hipotenusa