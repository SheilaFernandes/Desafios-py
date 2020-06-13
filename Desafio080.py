lista = list()
#c = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        print('Adicionado ao final da lista...')
    else:
        p = 0
        while True:
            if lista[c] < lista[p]:
                lista.insert(p, lista[c])
                lista.pop()
                print(f'Adicionado na posição {p} da lista ...')
                break
            elif p < len(lista) - 1:
                p += 1
#elif p == len(lista) - 1:
            else:
                print('Adicionado ao final da lista...')
                break
print(lista)

