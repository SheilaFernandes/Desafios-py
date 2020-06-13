lista = dict()
lista['Nome'] = str(input('Nome: '))
lista['Média'] = float(input('Média: '))
if lista['Média'] >= 7:
    lista['Situação'] = 'Aprovado'
else:
    lista['Situação'] = 'Reprovado'
#Existem duas formas de fazer. Acessando o dict atraves apenas da Keys() ou acesando-a diferenciando values() e keys()
#Acessando apenas através da Keys():
for c in lista:
    print(f'\033[1;33m{c} é igual {lista[c]}')
#acessando atraves de keys() e values():
for k, v in lista.items():
    print(f'\033[1;34m{k} é igual {v}')

