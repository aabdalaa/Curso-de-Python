n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end=(' '))
        tot += 1
    else:
        print('\033[31m', end=(' '))
    print('{}'.format(c), end=(' '))
print('\n\033[mO número {} foi dividido em {} vezes.'.format(n1, tot))
if tot == 2:
    print('por isso ele é um número PRIMO !')
else:
    print('por isso ele NÃO É PRIMO !')
