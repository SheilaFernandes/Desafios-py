nome = str(input('Digite seu nome: ')).strip()
print('No nome {:>^50}, tem o nome SILVA?'.format(nome), 'silva' in nome.lower())
# ou pode ser feito desta forma também >>>>> print(nome.upper().find('SILVA'))