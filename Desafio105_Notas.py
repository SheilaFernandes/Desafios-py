def notas(*valores, sit=False):
    dados = dict()
    dados['total'] = len(valores)
    dados['maior'] = max(valores)
    dados['menor'] = min(valores)
    dados['média'] = dados['total']/len(valores)

    if sit == True:
        if dados['média'] >= 7 :
            dados['situação'] = 'Boa'
        elif 6<= dados['média']> 7:
            dados['situação'] = 'Razoável'
        else:
            dados['situação'] = 'Ruim'
    return dados
print(notas(6,4,20, sit=True))
