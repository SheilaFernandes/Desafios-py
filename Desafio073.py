Lista = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atletico', 'Botafogo', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico - GO')
print('\033[1;33mLista do campeonato Brasileiro')
for c in range(0, len(Lista)):
    print(Lista[c])
print('{:-^25}'.format('-'))
print(f'\033[1;35mOs 5 primeiros times são {Lista[0:5]}\033[m')
b = Lista[-4:]
print('\033[1;36mOs 4 ultimos colocados são:', Lista[-4:], '\033[m')
for cont in range(0, len(b)):
    print('\033[1;35m', b[cont])
print('\033[1;31m', sorted(Lista))
print(f'\033[1;33m A Chapecoense esta na {Lista.index("Chapecoense")+1}ª')
