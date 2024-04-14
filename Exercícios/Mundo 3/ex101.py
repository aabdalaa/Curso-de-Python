from datetime import date
print('___'*20)
ano = int(input('EM QUE ANO VOCÊ NASCEU ? '))
def voto(anor):
    atual = date.today().year
    idade = atual - anor
    if idade < 16:
        print('___'*20)
        print(F'COM {idade} ANOS, VOCÊ AINDA NÃO PODE VOTAR !')
    elif 16 <= idade <= 17:
        print('___' * 20)
        print(F'COM {idade} ANOS, O VOTO É OPCIONAL !')
    elif 18 <= idade <= 64:
        print('___' * 20)
        print(F'COM {idade} ANOS, O VOTO É OBRIGATÓRIO !')
    elif idade >= 65:
        print('___' * 20)
        print(F'COM {idade} ANOS, O VOTO É OPCIONAL !')
    print('___'*20)

print(voto(ano))
