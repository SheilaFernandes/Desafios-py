cidade = str(input('Em que cidade você nasceu? ')).strip()

"""a = cidade.upper().split()
#para que a letra fique maiuscula é necessario fazer essa conversão antes de splitar a frase ou texto. Se tentar dá um
#upper em uma lista o programa retornar em erro. Talvez pela dificuldade de identificar cada letra em uma lista 
poderia ter criado uma variável 'a' para que eliminar o código digitado na linha 6 com vários metodos. Tudo denpende
da ordem dos métodos, pois o mesmo precisar ter uma sequencia logica de etapas de transformação a ser realizada na 
palavra ou frase.
Outro ponto observado é que não foi necessario colocar o comando 'print' antes do input. Se o 'print' for utilizado o
programa nao roda  >>>>> desafio 22 também foi feito assim. """

print('A cidade {} começa o nome SANTO? '.format(cidade), cidade.upper().split()[0] == 'SANTO')
#print(cid[:5].upper() == 'SANTO') >>>> Outra forma de fazer.