# A Variável ac foi colocada como '' pois assim ele não fará uma conta com os inputs que o usuário vai colocar.
# desta forma o Python vai identificar que cada input é uma palavra (p. ex) e os dados recebidos (pesos) poderão
# ser separados pelo método split()
ac = ''
for c in range(0, 5): #neste range poderia ter sido utilizado de 1 a 8.
    a = float(input('Peso da {}ª pessoa>>> '.format(c+1)))
    ac += str(a) + str(' ')
b = ac.split()
maior = b[0]
menor = b[0]
for v in range(0, 5): #aqui o range foi utilizado começando do zero, pois assim facilita a localização das posições dos pesos splitados.
#O If abaixo serve para substituir o número maior e não acumular como normalmente é utilizado. Assim, a cada teste de
# quais dos pesos é maior, a variável maior é substituida pelo ultimo valor maior testado. O racional utilizado para o menor.
    if float(maior) >= float(b[v]): #Para identificar quem é o maior número é necessario convertes para float (mesmo Type de a)
        maior = maior
    else:
        maior = b[v] #substituição do valor maior pelo maior valor identificado durante o print
for m in range(0, 5):
    if float(menor) <= float(b[m]):
        menor = menor
    else:
        menor = b[m]
print('O maior peso é >>>> {}'.format(maior))
print('O menor peso é >>>> {}'.format(menor))
