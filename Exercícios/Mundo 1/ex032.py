from datetime import date
ano = int(input('que ano quer analisar ? se quiser saber sobre o ano atual digite o número zero. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano BISSEXTO ! '.format(ano))
else:
    print('O ano {} não é um ano BISSEXTO '.format(ano))
