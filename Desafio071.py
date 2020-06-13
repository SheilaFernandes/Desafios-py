valor = int(input('Qual valor você quer sacar? R$'))
while True:
    total = 0
    nota50 = nota20 = nota10 = nota1 = 0
    if valor >= 50:
        nota50 = valor // 50
        resto50 = valor % 50
        total += nota50 * 50
        if total == valor:
            break
        else:
            if resto50 >= 20:
                nota20 = resto50 // 20
                resto20 = resto50 % 20
                total += nota20 * 20
                if total == valor:
                    break
                else:
                    if resto20 >= 10:
                        nota10 = resto20 // 10
                        resto10 = resto20 % 10
                        nota1 = resto10
                        total += nota10 * 10 + nota1
                        break
                    else:
                        nota1 = resto20
                        break
            elif resto50 >= 10:
                nota10 = resto50 // 10
                resto10 = resto50 % 10
                nota1 = resto10
                break
            elif resto50 >= 1:
                nota1 = resto50
                break
    elif valor >=20:
        nota20 = valor // 20
        resto20 = valor % 20
        total += nota20 * 20
        if total == valor:
            break
        else:
            if resto20 >= 10:
                nota10 = resto20 // 10
                resto10 = nota20 % 10
                nota1 = resto10
                total += nota10 * 10 + nota1
                break
            elif resto20 >= 1:
                nota1 = resto20
                total += nota1
                break
    elif valor >= 10:
        nota10 = valor // 10
        resto10 = valor % 10
        nota1 = resto10
        total += nota10 * 10 + nota1
        break
    elif valor >= 1:
        nota1 = valor
        total += nota1
        break
#if nota50 != 0  and nota20 != 0 and nota10 != 0 nota1 != 0:
print(f'Total de {nota50} cédulas de R$50')
print(f'Total de {nota20} cédulas de R$20')
print(f'Total de {nota10} cédulas de R$10')
print(f'Total de {nota1} cédulas de R$1')

