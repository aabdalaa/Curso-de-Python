'''print('-=-'*20)
print('LOJA SUPER BARATÃO')
print('-=-'*20)
n1 = ''
n2 = 0
n21 = 0
n22 = 0
n3 = ''
n4 = 0
barato = 0
barato1 = ''
while True:
    n1 = str(input('NOME DO PRODUTO: ')).lower().strip()
    print('-=-'*20)
    n2 = int(input('PREÇO: R$ '))
    n21 += n2
    if n2 > 1000:
        n22 += 1
    if n4 == 1 or n2 < barato:
        barato = n2
        barato1 = n1
    print('-=-' * 20)
    n3 = str(input('DESEJA CONTINUAR[S/N]: ')).lower().strip()
    print('-=-'*20)
    if n3 == 's':
        continue
    if n3 == 'n':
        break
print('----------- FIM DO PROGRAMA -----------')
print(f'O total da compra foi R$ {n21}')
print(f'temos {n22} produto custando mais de R$ 1000,00.')
print(f'O produto mais barato foi a(o) {barato1} e custa R$ {barato}.')'''

print('---'*20)
print('<' * 20, 'LOJA ANDRÉ', '>' * 20)
print('-=-'*20)
print('troque a virgula pelo ponto final !!!')
print('-=-'*20)
preco = continua = cont = contM = total = menor = 0
nome = barato = ''
while True:
    nome = str(input('DIGITE O NOME DO PRODUTO: ')).strip()
    print('-=-'*20)
    preco = float(input('PREÇO: R$ '))
    print('-=-'*20)
    continua = str(input('DESEJA CONTINUAR ? [S / N] ')).strip().upper()
    print('-=-'*20)
    cont += 1
    total += preco

    if preco > 1000:
        contM += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    if continua == 'S':
        continue
    elif continua == 'SIM':
        continue
    elif continua == 'N':
        break
    elif continua == 'NÃO':
        break
    else:
        print('Resposta inválida.')
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'O Total gasto na compra foi de R$ {total :.2f}')
print(f'A compra possui {contM} Produto(s), que custa(m) mais de R$ 1000,00.')
print(f'E o Produto mais barato é {barato} com o custo de R$ {menor :.2f}')
