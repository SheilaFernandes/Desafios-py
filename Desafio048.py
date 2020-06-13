soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        #Acumulador soma outra forma de representar a formula abaixo soma += c
        soma = soma + c
        #Contador de números outra forma de representar a formula abaixo cont += 1
        cont = cont + 1
        print(c, end='-')
print('\n')
print('\033[1;36m-------'*6)
print('\033[1;35mA Soma dos {} números  é {}'.format(cont, soma))
print('\033[1;36m--FIM--'*6)
