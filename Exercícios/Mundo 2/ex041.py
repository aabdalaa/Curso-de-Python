from datetime import date
atual = date.today().year
n1 = int(input('ano de nascimento do atleta: '))
n2 = atual - n1
print('o atleta tem {} anos de idade.'.format(n2))
if n2 <= 9:
    print('classificação: MIRIM. ')
elif n2 <= 14:
    print('classificação: INFANTIL. ')
elif n2 <= 19:
    print('classificação: JÚNIOR. ')
elif n2 == 25:
    print('classificação: SÊNIOR. ')
elif n2 > 25:
    print('classificação: MASTER. ')
