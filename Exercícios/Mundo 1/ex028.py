from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 20)
print('pensei em um número de 0 a 5, tente adivinhar meu número.')
print('-=-' * 20)
jogador = int(input('em que número de 0 a 5 eu pensei ? '))
print('PROCESSANDO...')
sleep(5)
if jogador == pc:
    print('Parabéns você pensou o mesmo número que eu !')
    print('Eu pensei no número {}.'.format(pc))
else:
    print('Pewww, você errou o número, eu pensei no número {}'.format(pc))
