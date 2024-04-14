from random import randint
from time import sleep
dicio = {'jogador 1': randint(1, 6),
         'jogador 2': randint(1, 6),
         'jogador 3': randint(1, 6),
         'jogador 4': randint(1, 6)}
rank = dict()
p = 0
c = range(1, 5)
for k, v in dicio.items():
    print(f'O {k} tirou {v} no dado !')
    sleep(1)
print('-=-'*20)
rank["ordem"] = dicio
mami = sorted(dicio.items())
print('=== RANKING DOS JOGADORES ===')
for k, v in mami:
    p += 1
    print(f'{p}º LUGAR: {k} com o número {v} no dado.')
    sleep(1)
