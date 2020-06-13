d = float(input('Digite a distância da viagem que deseja fazem em KM: '))
if d <= 200:
    print('O preço da sua passagem é R$ {:.2f}!'.format(d * 0.50))
else:
    print('O preço da sua passagem é R$ {:.2f}'.format(d * 0.45))
