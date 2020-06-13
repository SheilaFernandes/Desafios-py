somaT = 0 #soma de todas as idades
contM = 0 #contador de mulheres com menos de 20 anos
h = '' #lista dos nomes dos homens
hv = '' #Nome do homem mais velho.
lidh = '' #lista de idades dos homens
for c in range(1, 5):
    n = str(input('\033[1;34mPRIMEIRO NOME da {}ª pessoa: '.format(c))).strip()
    id = int(input('Idade da {}ª pessoa: '.format(c)))
    s = str(input('[F] Feminino\n[M] Masculino\nSexo da {}ª pessoa: '.format(c))).strip()
    print('\033[1;33m-'*35)
    somaT += id
    if s.lower() == str('m'):
        h += n +str(' ') #forma a lista de nomes dos homens
        lidh += str(id) + str(' ') #forma a lista de idades na mesma ordem respectiva da lista de nomes dos homens.
    elif id < 20: #valida se a mulher tem menos de 20 anos.
        contM += 1 # caso tenha menos de 20 anos, acrescenta ela no contador.
a = h.split()
b = lidh.split()
maior = b[0]
for m in range(0, len(a)):
    if float(maior) > float(b[m]):
        maior = maior
    else:
        maior = b[m]
        hv = a[m]
print('A Média das idades é {:.2f}'.format(somaT/4))
print('O homem mais velho é {} e tem {} anos de idade'.format(hv.title(), maior))
print('Dentre a lista de pessoas acima, {} mulhere(s) tem menos de 20 anos'.format(contM))

