a = float(input('1ª distancia de uma reta:'))
b = float(input('2ª distancia de uma reta: '))
c = float(input('3ª distancia de uma reta: '))
if (a + b > c and a + c > b and b + c > a):
    print('As medidas PODEM FORMAR um triangulo!')
else:
    print('não formam triangulo')
print('>>>>>Fim>>>>>')
