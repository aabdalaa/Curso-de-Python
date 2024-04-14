maior = 0
menor = 0
print('troque a virgula pelo ponto !')
print('-=-'*20)
for p in range(1, 6):
    peso = float(input('digite o {}° peso: '.format(p)))
    print('-=-'*20)
    if p == 1:
        maior = peso
    if p == 1:
        menor = peso
    elif peso:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o menor peso lido foi de {} kg !'.format(menor))
print('o maior peso lido foi de {} kg !'.format(maior))
