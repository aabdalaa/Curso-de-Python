jog = dict()
li = list()

nam = str(input('Nome do jogador: '))
prt = int(input(f'Quantas partidas {nam} jogou ? '))
jog["nome"] = nam
for c in range(1, prt + 1):
    li.append(int(input(f'Quantos gols {nam} fez na {c}º partida ? ')))
jog["gols"] = li[:]
jog["total"] = sum(li)

print('-=-'*20)
print(jog)
print('-=-'*20)
print(f'O campo nome tem o valor {jog["nome"]}.')
print(f'O campo gols tem o valor {jog["gols"]}.')
print(f'O campo total tem o valor {jog["total"]}')
print('-=-'*20)
print(f'O jogador {nam} jogou {prt} partidas.')
for i, v in enumerate(jog['gols']):
    print(f'=> Na partida {i + 1}, fez {v} gols.')
print(F'Foi um total de {jog["total"]} gols.')
print('-=-'*20)
