somaidade = 0
media = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(('----{}ª PESSOA ----'.format(c)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade = '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
media = somaidade / 4
print('A média das idades é {}'.format(media))
print('O homem mais velho é {} e tem {} anos'.format(nomevelho, maioridade))
print('Ao todo {} mulher com menos de 20 anos.'.format(totmulher20))
