a = float(input('1º lado do triangulo >>> '))
b = float(input('2º lado do triangulo >>> '))
c = float(input('3º lado do triangulo >>> '))
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('As medidas informadas formam um triangulo equilátero.')
    elif a == b or a == c or b == c:
        print('As medidas informadas formam um triangulo isóceles.')
    elif a != b and a != c and b != c:
        print('As medidas informadas forma um triangulo escaleno')
else:
    print('As medidas informadas NÃO FORMAM é triangulo')