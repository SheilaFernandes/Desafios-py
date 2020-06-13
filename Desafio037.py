n = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:\n'
      '[1] converter para o BINÁRIO\n'
      '[2] converter para OCTAL\n'
      '[3] converter para HEXADECIMAL\n')
o = int(input('Sua opção: '))
if o == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido para OCTAL é igua a  {}'. format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida')
#faz-se o fatiamento por que todos os tipos de números no Python começa
# com 0b, 0x, etc... então manda mostrar a partir do 2ª para tirar esta
# identificação interna do python