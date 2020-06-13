a = input('digite uma frase sem acentos>>> ').strip().upper()
y = a.split()
junto = ''.join(y)
b = len(junto) -1 #retorna no comprimento da frase com espaços e o -1 é para mostrar a ultima posição (de 0 até a ultima posição).
# variável vazia para receber a frase invertida (acumulador)
#nova = ''
nova = junto[::-1]
"""for c in range(b, -1, -1):
    nova += junto[c]"""
if junto == nova:
    print('A frase é um POLIDRONO ... veja ...')
else:
    print('A frase não é um POLIDRONO ... veja ...')
print('\033[1;34m-'*35)
print('\033[1;32m {}'.format(nova.upper()))
print('\033[1;34m-'*35)
