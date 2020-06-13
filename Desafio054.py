from datetime import date
cont = 0
maiores = ''
NaoMaiores = ''
for c in range(1, 8):
    a = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - a < 21:
        cont += 1
        NaoMaiores += str(c) + str('-')
    else:
        maiores += str(c) + str('-')
if cont == 1:
    print('\033[1;32m{} pessoa não atingiu a maioridade'.format(cont))
    print('Pessoa que não é maior: {}'.format(NaoMaiores))
    print('\033[1;35m{} Pessoas já são maiores'.format(7-cont))
    print('Pessoas maiores: {}'.format(maiores))
elif cont == 7:
    print('\033[1;32m Todas as pessoas não atingiram a maioridade')
elif cont == 6:
    print('\033[1;32m{} pessosas não atigiram a maioridade'.format(cont))
    print('Pessoas não maiores: {}'.format(NaoMaiores))
    print('\033[1;35m{} pessoa já é maior'.format(7-cont))
    print('Pessoa maior: {}'.format(maiores))
elif cont == 0:
    print('\033[1;35m Todas já são maiores')
else:
    print('\033[1;32m{} pessoas não atingiram a maioridade'.format(cont))
    print('Pessoas não maiores: {}'.format(NaoMaiores))
    print('\033[1;35m{} pessoas já são maiores'.format(7 - cont))
    print('Pessoas maiores: {}'.format(maiores))

