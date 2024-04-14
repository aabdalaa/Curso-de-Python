from datetime import date

atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print('quem nasceu no ano {} tem {} anos de idade no ano {}.'.format(nasc, idade, atual))
saldo = idade - 18
saldo2 = 18 - idade
if idade == 18:
    print('Você tem que se alistar imediatamente ! ')
elif idade < 18:
    print('ainda faltam {} anos para você se alistar !'.format(saldo2))
elif idade > 18:
    print('Você tinha que ter se alistado a {} anos.'.format(saldo))
