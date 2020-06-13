# Faça um programa que leia a largura e a altura de uma parede em metros calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
n1 = float(input('Informe a largura da parede em metros >>>'))
n2 = float(input('Informe a altura da parede em metros >>> '))
A = n1 * n2
T = A/2
print('Você precisa de {} litros de tinta para pintar a parede com as dimensões '
      'informadas ({}x{}m).'.format(T, n1, n2))
# QUANTO MENOS VARIÁVEIS UTILIZAR MENOS MEMORIA O PROGRAMA VAI UTILIZAR PARA EXECUTAR!!!!