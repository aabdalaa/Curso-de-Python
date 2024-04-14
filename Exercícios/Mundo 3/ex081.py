lista = []
continua = 0
while True:
    lista1 = int(input('Digite um valor: '))
    print('---'*20)
    if lista1 not in lista:
        lista.append(lista1)
    else:
        print('Valor duplicado... Não posso colocar !')
    print('valor adicionado com sucesso !')
    continua = str(input('Deseja continuar [S/N]: ')).upper()
    print('---'*20)
    if continua == 'S':
        continue
    elif continua == 'SIM':
        continue
    elif continua == 'N':
        break
    elif continua == 'NÃO':
        break
print(f'Foram digitados {len(lista)} números !')
print('---'*20)
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
print('---'*20)
if 5 in lista:
    print('O número 5 está presente !')
else:
    print('O número 5 não está presente !')
