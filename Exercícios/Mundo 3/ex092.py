lol = dict()
est = str(input('Nome: '))
lol["nome"] = est
anon = int(input('Ano de Nascimento: '))
lol["idade"] = 2019 - anon
mark = lol["idade"]
cart = int(input('Carteira de trabalho, (se não tiver digite 0): '))
if cart == 0:
    print('-=-'*20)
    print(f'- Seu nome é {est}.')
    print(f'- Sua idade é: {lol["idade"]} ano(s).')
    print(f'- Sua ctps tem o valor: {cart}.')
else:
    anoc = int(input('Ano de contratação: '))
    sal = float(input('Salário: R$'))
    print('-=-'*20)
    print(f'- Seu nome é: {est}.')
    print(f'- Sua idade é: {lol["idade"]} ano(s).')
    print(f'- Seu ctps tem o valor: {cart}.')
    print(f'- Sua contratação foi em: {anoc}.')
    print(f'- O salário atual é: R${sal}.')
    var = 62 - mark
    print(f'- Falta {var} anos para poder se aposentar.')
