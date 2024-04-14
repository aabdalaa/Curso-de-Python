lista = []
continua = 0
while True:
    lista1 = int(input('Digite um valor: '))
    print('---'*20)
    if lista1 not in lista:
        lista.append(lista1)
    else:
        print('Valor duplicado... Não posso colocar !')
        print('---'*20)
    print('valor adicionado com sucesso !...')
    print('---'*20)
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
lista.sort()
print(F'VOCÊ DIGITOU OS NÚMEROS: {lista}')
