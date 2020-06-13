lista = list()
expressao = input('Digite uma expressão>>> ')
for c in range(0, len(expressao)):
    lista.append(expressao[c])
if lista.count('(') == lista.count(')'):
    print('Sua expressão esta válida')
else:
    print('Sua expressão não é válida')

print('\033[1;34m:-^20'.format('-'))
print(expressao.split())
print(expressao[2])
print(expressao.count('('))
print(len(expressao.split()))
