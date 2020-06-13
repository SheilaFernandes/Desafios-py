v = float(input('Informe a veolocidade do que o carro esta percorrendo >>> '))
if v > 80:
    print('Você foi multado!! O valor da sua multa é de R${:.2f}.'.format((v - 80) * 7))
else:
    print('ok sem multa!!!')
