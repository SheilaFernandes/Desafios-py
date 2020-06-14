def ficha(n= '<desconhecido>', g = 0):
    return f'O jogador {n.title()}, fez {g} gol(s) no campeonato.'

#Programa Principal:
nome = str(input('Nome do Jogador: '))
'''A variável gols foi registrada como str para que a variável seja aceita vazia'''
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
'''retira os espaços para validar se a variável esta vazia.'''
if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
