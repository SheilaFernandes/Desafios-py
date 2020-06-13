n = 0
while True:
    c = 1
    print('\033[1;34m-'*25)
    n = int(input('\033[1;36mQuer ver a tabuada de qual valor? '))
    print('\033[1;34m-'*25)
    if n <= 0:
        break
    else:
        while c <=10:
            r = n * c
            print(f'\033[1;34m{n} x {c:2} = {r}')
            c += 1
print('\033[1;31mFim do programa!!!')
