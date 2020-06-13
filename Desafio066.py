num = cont = soma = 0
while True:
    num = int(input('Digite um número (Caso queira parar digite 999) >>> '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print('\033[1;33m--'*40)
if cont == 1:
    print(f'Você digitou {cont} numero e a soma é {soma}')
else:
    print(f'Você digitou {cont} números e a soma entre eles é {soma}')
print(f'\033[1;33mFIM')
