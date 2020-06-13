'''nome = 'João'
sobrenome = 'Silva'
idade = '30'
resultado = (nome + ' ' + sobrenome + ' ' + 'terá' + ' ' + idade + ' ' + 'anos')
resultados = (nome + sobrenome + 'terá' + idade + 'anos')
print(resultado)
print(resultados)'''

a = [{'nome': 'lucas', 'gols': [2, 3, 4], 'peso': 58}, {'nome': 'Sheila', 'gols': [21, 0, 1], 'peso': 40}]
print(a[0])
for p, c in enumerate(a[0]['gols']):
    print(p, c)
