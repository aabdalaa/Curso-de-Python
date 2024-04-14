"""for c in range(1,101):
    print(' {} -'.format(c), end=(''))
print(' fim')'''

'''c = 1
while c < 11:
    print(c)
    c += 1
print('fim')'''

'''for c in range(0, 2):
    int(input('digite um valor: '))
print('fim')'''

'''for c in range(0, 5):
    int(input('digite um valor: '))
print('FIM !')'''

'''r = 'S'
while r == 'S':
    c = int(input('digite um valor: '))
    r = str(input('quer continuar ? [S/N]: ')).upper()
print('FIM !')'''

impar = 0
par = 0
r = 'S'
while r == 'S':
    c = int(input('digite um valor: '))
    r = str(input('quer continuar ? [S/N]: ')).upper()
    if c % 2 == 0:
        par += 1
    else:
        impar += 1
print('''você escreveu {} números pares,
e {} números impares'''.format(par, impar))
print('-=-'* 20)
print('FIM !')"""
