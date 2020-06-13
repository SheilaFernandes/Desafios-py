lista = list()
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp[:])
    temp.clear()
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg in 'N':
        break
    while True:
        if perg not in 'SN':
            perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        else:
            break
print(f'\033[1;34m{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('{:-<26}'.format('-'))
for p, c in enumerate(lista):
    m = (lista[p][1] + lista[p][2]) / 2
    print(f'{p:<4} {lista[p][0]:<15} {m}')
print('-\033[1m' * 26)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    while True:
        if aluno > (len(lista) - 1) and aluno != 999:
            aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        else:
            break
    if aluno == 999:
        break
    else:
        print(f'Notas de {lista[aluno][0]}, são {lista[aluno][1:]}')
        print('{:-<50}'.format('-'))

