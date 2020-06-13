from time import sleep
# Esquema de cores
cor = {'Azul': '\033[1;34m',
       'Roxo' : '\033[1;35m',
       'Amarelo' : '\033[1;33m',
       'Vermelho' : '\033[7;31;40m',
       'Texto' : '\033[1;30m',
       'limpa' : '\033[m'}

casa = float(input('{}Qual o valor do imóvel a ser comprado?{} R$ '.format(cor['Texto'],  cor['Azul'])))
salario = float(input('{}Qual o valor do seu salário mensal? {}R$ '.format(cor['Texto'], cor['Azul'])))
tempo = int(input('{}Em quantos anos você deseja pagar o valor da casa?{} '.format(cor['Texto'], cor['Azul'])))
A = casa / (tempo*12)
print('{}Analisando sua solicitação...'.format(cor['Amarelo']))
sleep(1)
print('{}...{}'.format(cor['Amarelo'], cor['limpa']))
sleep(3)
if A > salario * 0.30:
    print('{}Infelizmente sua solicitação não pode ser aprovada!{}'.format(cor['Vermelho'], cor['limpa']))
else:
    print('{}PARABENS!!!{}\n{}Você terá o valor de {} R$ {}{} na sua conta em {}30 minutos{}'.format(cor['Roxo'], cor['limpa'],
        cor['Roxo'],cor['Azul'], casa, cor['Roxo'],'\033[4m', cor['limpa']))