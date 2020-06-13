dic = dict()
pessoas = list()
soma = media = 0
while True:
    dic.clear()
    dic['nome'] = str(input('Nome: '))
    while True:
        dic['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if dic['sexo'] not in 'FM':
            print('Por favor, digite apenas F ou M.')
        else:
            break
    dic['idade'] = int(input('Idade: '))
    soma += dic['idade']
    pessoas.append(dic.copy())
    while True:
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if op not in 'SN':
            print('Por favor digite apenas S ou N.')
        else:
            break
    if op in 'N':
        break
print(f'\033[1;34m- O grupo tem {len(pessoas)} pessoas.')
'''for c in pessoas:
    soma += c['idade']'''
media = soma / len(pessoas)
print(f'As mulheres cadastras foram ', end='')
for v in pessoas:
    if v['sexo'] == 'F':
        print(v['nome'], end=' ')
print(f'\nA média de idade é {media} anos.')
print(f'A lista de pessoas que estão acima da média:')
for k in pessoas:
    for i, p in k.items():
        if k['idade'] > media:
            print(f'    {i:^6} = {p:^10}; ', end='')
    print()
print('ENCERRADO')
print(dic)
print(pessoas)