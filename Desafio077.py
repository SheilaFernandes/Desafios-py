tupla = ('aprender', 'sorrir', 'estudar', 'grátis', 'pincél', 'curso', 'parár')
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiouáíóúà':
            print(letra, end=' ')
