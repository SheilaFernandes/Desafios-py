nome = str(input('Digite um nome completo: ')).strip()
nome = nome.title().split()
#print(nome)
print('Muito prazer em te conhecer {}'.format(nome))
print('Primeiro nome >>> {}'.format(nome[0]))
print('Ultimo nome >>>> {}'.format(nome[(len(nome)-1)]))
