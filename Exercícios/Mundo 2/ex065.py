media = 0
n = 0
c = 0
soma = 0
maior = 0
menor = 0
g = 'S'.upper()
while g == 'S':
    c = int(input('digite um número: '))
    g = str(input('Deseja continuar[S/N]? ')).upper()
    n += 1
    soma += c
    if n == 1:
        maior = menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
media = soma / n
if g == 'N':
    print('''    você digitou {} números e a media foi {}
    o menor valor foi {} e o maior foi {}.'''.format(n, media, menor, maior))
