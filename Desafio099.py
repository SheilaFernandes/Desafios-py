from time import sleep
def maior(* n):
    print('Analisando os valores passados ...')
    sleep(0.5)
    m = 0
    for p, c in enumerate(n):
        print(f'{c} ', end='')
        if p == 0:
            m = c
        elif m < c:
            m = c
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {m}')
    print('-' * 60)
#Programa Principal:
maior(500, 9, 2, 6, 0, 100, 200)
maior(4, 0, 2)
maior(1, 2)
maior(6)
maior()
