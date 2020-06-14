from time import sleep
def contador(Inicio, Fim, Passo):
    print(f'Contagem de {Inicio} até {Fim} de {abs(Passo)} em {abs(Passo)}')
    sleep(1)
    if Passo > 0:
        for c in range(Inicio, Fim+1, Passo):
            print(f'{c} ', end='')
            sleep(0.25)
        print('FIM')
        print('-' * (abs(Fim) * 3))
    elif Passo < 0:
        for c in range(Inicio, Fim - 1, Passo):
            print(f'{c} ', end='')
            sleep(0.25)
        print('FIM')
        print('-' * abs(Fim) * 3)

#Programa Principal:
contador(1, 10 , 1)
contador(10, 0, -2)
print('_' * 20)
print('Agora é a sua vez de personalizar a contagem!')
I = int(input('Inicio: '))
F = int(input('Fim: '))
P = int(input('Passo: '))
if P == 0 and I < F:
    P = 1
elif P == 0 and I > F:
    P = -1
elif P > 0 and I > F:
    P *= -1
elif P < 0 and I < F:
    P *= -1
contador(I, F, P)


