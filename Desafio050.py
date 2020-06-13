soma = 0
cont = 0
print('\033[1;31m-\033[1;35m'*35)
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        cont += 1
        soma += n
print('\033[1;34m='*45)
print('\033[1;33mQuantidade de números pares informados: {}\nA soma dos números pares mostrados é {}'.format(cont, soma))
print('\033[1;34m='*45)
