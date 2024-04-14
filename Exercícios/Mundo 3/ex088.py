from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('        JOGA NA QUINA           ')
print('-'*30)
jogo = int(input('Quantos jogos deseja fazer ? '))
print()
print('-'*30)
ko = int(input('Quantos números terá o seu jogo ? '))
print()
tot = 1
while tot <= jogo:
    cont = 0
    while True:
        h = randint(1, 80)
        if h not in lista:
            lista.append(h)
            cont += 1
        if cont >= ko:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=-'*10, f'/ SORTEANDO {jogo} JOGOS... /', '-=-'*10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
