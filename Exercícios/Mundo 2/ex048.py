soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} números abaixo é igual a: {}.'.format(cont, soma))
print('Os números são :')
for b in range(1, 500, 2):
    print('-=-'*20)
    print(b)
