from random import randint
from time import sleep
print('-=-'*20)
print('{:^60}'.format('Pedra, Papel ou Tesoura'))
print('-=-'*20)
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
p = int(input('Qual a sua jogada? '))
pc = randint(1, 3)
lista = ('pedra', 'papel', 'tesoura')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
if p == pc:
    print('Empate Computador escolheu {}'.format(lista[pc-1]))
elif p == 1 and pc == 2:
    print('Você Perdeu, Eu escolhi PAPEL e você escolheu PEDRA !')
elif p == 1 and pc == 3:
    print('Você Ganhou!!!, Eu escolhi TESOURA e você escolheu PEDRA!')
elif p == 2 and pc == 1:
    print('Você Ganhou!!!, Eu escolhi PEDRA e você escolheu PAPEL !')
elif p == 2 and pc == 3:
    print('Você Perdeu, Eu escolhi TESOURA e você escolheu PAPEL !')
elif p == 3 and pc == 1:
    print('Você Perdeu, Eu escolhi PEDRA e você escolheu TESOURA !')
elif p == 3 and pc == 2:
    print('Você Ganhou!!!, Eu escolhi PAPEL e você escolheu TESOURA !')
else:
    print('[ERRO] JOGADA INVÁLIDA !')
