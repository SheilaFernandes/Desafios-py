def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m²')
def lin():
    print('\033[1;34m-'*30)
#Programa Principal
lin(), print('     Controle de Terrenos'), lin(), print('\33[m')
area(l=float(input('Largura (m): ')), c=float(input('Comprimento (m): ')))
