def notas(*valores, sit=False):
    """
    -> Função para analisar notas e situações
    :param valores: notas a serem analisadas
    :param sit: valor apcional para visualizar a situação do aluno
    :return: retorna a quantidade de notas analisadas, maior nota, menor nota, media das notas e a situação do aluno
    """

    dados = dict()
    dados['total'] = len(valores)
    dados['maior'] = max(valores)
    dados['menor'] = min(valores)
    dados['média'] = sum(valores)/len(valores)

    if sit:
        if dados['média'] >= 7 :
            dados['situação'] = 'Boa'
        elif dados['média']>= 5:
            dados['situação'] = 'Razoável'
        else:
            dados['situação'] = 'Ruim'
    return dados
print(notas(5.5,2.5 ,8.5, sit=True))
