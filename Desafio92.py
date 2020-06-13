from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome:'))
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
pessoa['idade'] = idade
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
print('\033[1;36m-' * 35)
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contração: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    print('-' * 35)
    for k, c in pessoa.items():
        print(f'{k} tem valor {c}')
    aposentadoria = pessoa['contratação'] - ano + 35
    print(f'aposentadoria tem o valor {aposentadoria}')
else:
    print('\033[1;36m-' * 35)
    for k, c in pessoa.items():
        print(f'{k} tem valor {c} ')

