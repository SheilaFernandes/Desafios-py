def fatorial(n, show=False):
    """
    >>> Calcula o faturial de um número (n)
    :param n: numeró a ser realizado o calculo de fatorial
    :param show (opcional): Caso desejar que a memória de calculo seja mostrada, preencher show=True.
    O Campo é opcional.
    :return: retorna o valor final do fatorial do número n
    by Sheila Fernandes
    """

    print(f'{n} ', end='')
    '''Variavel criada para acumular o valor final do fatorial'''
    fat = 1
    for c in range(n , 0, -1):
        '''If show = True vai mostrar a memoria de calculo'''
        if show:
            '''linha 17 para evitar que o número n seja repetido 2x'''
            if c != n:
                print(f'x {c} ', end='')
        fat *= c
    print('=', end=' ')
    '''por boas praticas, uma função nao exibe um valor (de modo geral), o ideal é apenas return of valor e a exibição
    do valor no console para o usuário deve realizada fora da função, conforme linha 27'''
    return fat

#Programa Principal
print(fatorial(5, show=True))
'''Exibição do menu interactive help criada logo no inicio da função.'''
help(fatorial)