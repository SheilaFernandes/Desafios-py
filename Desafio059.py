x = float(input('\033[1;31mDigite o 1º valor >>> '))
y = float(input('Digite o 2º Valor >>> '))
a = 0
while a != 5:
      print('\033[1;33m---'*15)
      print('[1] somar\n'
            '[2] Multiplicar\n'
            '[3] Maior\n'
            '[4] Novos números\n'
            '[5] sair do programa')
      print('---'*15)
      a = int(input('Escolha uma das opções do menu acima >>> '))
      if a == 1:
            soma = x + y
            print('\033[1;34mA soma é >>> {:.1f}\033[m'.format(soma))
      elif a == 2:
            mult = x * y
            print('\033[1;34mA multiplicação é >>> {:.1f}\033[m'.format(mult))
      elif a == 3:
            if x != y:
                  if x > y:
                        print('\033[1;34mO maior número é --- {:.1f}\033[m'.format(x))
                  else:
                        print('\033[1;34mO maior número é --- {:.1f}\033[m'.format(y))
      elif a == 4:
            x = float(input('\033[1;33mPrimeiro valor >>> '))
            y = float(input('Segundo valor >>> \033[m'))
      elif a == 5:
            print('\033[1;31mAté logo!!!')
