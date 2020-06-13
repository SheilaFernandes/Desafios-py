# Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros.
x = float(input('Digite um valor >>> '))
c = x *100
m = x *1000
print('{} metros equivalem à:\n{:.2f}cm\n{:.2f}mm\n{:.2f} dam\n{:.2f}hm\n'
       '{:.2f}km.\nCerto!!!!!'.format(x, c, m, (x/10), (x/100), (x/1000)))
