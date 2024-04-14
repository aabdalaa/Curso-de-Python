from random import randint
lis = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
soma = 0
def fed(d):
    print(f'sorteando {len(lis)} valores da lista: {lis}, PRONTO ! ')
    print('--'*30)
    print(d)

for val in lis:
    if val % 2 == 0:
        soma += val
fed(f'Somando os valores pares de: {lis}, temos {soma}')
