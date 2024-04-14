print('SEQUÊNCIA DE FIBONACCI v1.0 ')
print('-=-'*20)
n = int(input('quantos termos você deseja mostrar ? '))
t1 = 0
t2 = 1
print('~'*30)
print('')
print('{} -> {} ->'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' {} ->'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM ! ')
print('')
print('=-=--=-=-=-=-=-=-=-= VOLTE SEMPRE ! =-=-=-=-=-=-=-=-=-=-=-=-=')
