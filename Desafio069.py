i = h = m = p = 0 #pessoas com mais de 18 anos.
h = 0 # quantidade de homens.
m = 0 # quantidade de mulhere com menos de 20 anos.
p = 0 # numero de pessoas cadastradas.
print('\033[1;33m--' * 20)
while True:
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M] >>> ')).strip().upper()[0]
    idade = int(input('Idade >>> '))
    op = ' '
    while op not in 'SN':
        op = input('Deseja continuar? [S/N] ').strip().upper()[0]
        print('\033[1;33m--'*20)
    p += 1
    if sexo == 'F' and idade < 20:
        m += 1
    else:
        h += 1
    if idade > 18:
        i += 1
    if op == 'N':
        break
print(f'\033[1;34mDa lista de {p} pessoas que você cadastrou temos:')
if m == 1:
    print(f'{i} pessoa com mais de 18 anos.')
else:
    print(f'{i} pessoas com mais de 18 anos')
if h == 1:
    print(f'{h} homem.')
else:
    print(f'{h} homens.')
if m == 1:
    print(f'{m} Mulher com menos de 20 anos.')
else:
    print(f'{m} Mulheres com menos de 20 anos.')
