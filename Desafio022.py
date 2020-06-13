"""nome = input('digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
a =nome.split()
b = nome[0:]
print(len(b) - nome.count(' '))
print(len(a[0]))"""

#print(len(a[-1]) + len(a[1]) + len(a[2]) + len(a[3]) + len(a[4]))
# a contagem de todos as letras sem espaços não pode ser feita atraves do método split(), pois o mesmo conta ou
# a quantidade de letras do item ou a quantidade de itens da lista. Se for colocado um número de len grande para conseguir
# contar varios sobrenomes quando o nome tiver menos sobrenomes o programa vai dar erro e se tiver mais do que a pessoa
# escreveu o programa vai contar no maximo a quantidade de sobrenomes que tiver no código.
#o primeiro código (acima) é a pior opção pois consome mais memoria, o código abaixo é mais enxuto e usa apenas uma variavel
#nome que na linha 17 nao foi utilizado o comando print.... se usar o programa nao roda


nome = str(input('digite seu nome completo: ')).strip()
print('Seu nome Maiusculo é: {}'.format(nome.upper()))
print('Seu nome Minusculo é: {}'.format(nome.lower()))
print('Seu nome todo tem {} letras.'.format(len(nome[0:]) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(nome.capitalize().split()[0], len(nome.split()[0])))
