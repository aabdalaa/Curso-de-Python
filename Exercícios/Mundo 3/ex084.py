pessoas = list()
part2 = list()
quant = 0
while True:
    quant += 1
    pessoas.append(float(input('peso: ')))
    print('-=-'*20)
    pessoas.append(str(input('Nome: ')))
    print('-=-'*20)
    part2.append(pessoas[:])
    pessoas.clear()
    s = str(input('Deseja continuar [S/N] ? ')).upper()
    if s == 'S':
        print('-=-' * 20)
    if s == 'N':
        break
print('-=-'*20)
print(f'{quant} Pessoas foram cadastradas !')
print('-=-'*20)
print(f'O menor peso foi {min(part2)} KG. O menor peso foi de: ', end='')
for p in part2:
    if p[0] <= 85:
        print(f'{p[1]}. ', end='')
print(f'\nO maior peso foi {max(part2)} KG. O maior peso foi de: ', end='')
for p in part2:
    if p[0] >= 86:
        print(f'{p[1]}. ', end='')
print()
