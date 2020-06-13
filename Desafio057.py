s = str(input('Digite seu sexo [F] Feminino [M] Masculino:')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Opção inválida! Informe seu sexo: ')).strip().upper()[0]
print('Sexto {} registrado com sucesso'.format(s))
