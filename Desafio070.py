total = 0 #Valor total da compra
c = 0 #Quantidade de produtos comprados
p = 0
nome = ' '
MaisdeMil = 0
while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    p = float(input('Preço: R$'))
    c += 1
    total += p
    if c == 1:
        ProdutoMaisBarato = nome  # Nome do produto mais barato
        PMaisBarato = p  # Preço do Produto mais barato
    else:
        if p < PMaisBarato:
            PMaisBarato = p
            ProdutoMaisBarato = nome
        else:
            PMaisBarato = PMaisBarato
            ProdutoMaisBarato = ProdutoMaisBarato
    if p > 1000:
        MaisdeMil += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('\033[1;31m{:-^60}'.format('Fim do programa'))
print(f'\033[1;34mO total da sua compra foi {total} e você comprou {c} produtos.\n{MaisdeMil} produto(s) custaram mais R$1000,00.')
print(f'O produto mais barato é o {ProdutoMaisBarato} que custa R${PMaisBarato}')

