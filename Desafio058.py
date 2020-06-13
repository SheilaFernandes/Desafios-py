from random import randint
a = randint(0, 10)
cont = 1
print('\033[1;34m=='*35)
b = int(input('já pensei em um número inteiro de 0 a 10. \nQual número você acha que eu pensei?? '))
print('\033[1;34m=='*35)
while a != b:
    if a > b:
        b = int(input('\033[1;33mMais ... Tente novamente >>> '))
    else:
        b = int(input('\033[1;33mMenos ... Tente novamente >>> '))
    cont += 1
print('\033[1;31mVocê Acertou na {} ª tentativa'. format(cont))
