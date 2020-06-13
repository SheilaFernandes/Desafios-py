p = float(input('Informe o preço:R$'))
print('Qual a condição de pagamento deseja utilizar?\n'
      '[1] à vista no DINHEIRO \n'
      '[2] à vista no CARTÃO\n'
      '[3] em até 2x no CARTÃO DE CRÉDITO \n'
      '[4] 3x ou mais no CARTÃO DE CRÉDITO\n')
a = int(input('Informe uma das opções acima de acordo com a forma de pagamento que desejar:'))
if a == 1:
    print('O valor a ser pago com pagamento à vista no DINHEIRO é R${}'.format(p * 0.90))
elif a == 2:
    print('O valor  final a ser pago com pagamento à vista no CARTÃO É R${}'.format( p * 0.95))
elif a == 3:
    print('O valor a ser pago com o pagamento em até 2x NO CARTÃO DE CRÉDITO é R${}'.format(p))
    print('O valor das parcelas é 2x de R${}'.format((p) / 2))
elif a == 4:
    b = int(input('Quantas parcelas?'))
    print('O valor a ser pago com o pagamento em 3x ou mais no CARTÃO DE CRÉDITO é R${}'.format(p * 1.20))
    print('O valor das parcelas é de {}x de R${}'.format(b, (p * 1.20)/b))
else:
    print('Opção inválida, escolha outra opçaõ!')