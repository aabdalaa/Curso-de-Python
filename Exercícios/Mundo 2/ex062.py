print('TERMOS DE UMA P.A')
print('-=-'*20)
n1 = int(input('digite o primeiro termo: '))
n2 = int(input('digite a razão: '))
termo = n1
contador = 1
total = 0
c = 10
while c != 0:
    total = total + c
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += n2
        contador += 1
    print('PAUSA !')
    c = int(input('Quantos termos você quer mostrar a mais ? '))
print('FIM !')
print('progressão mostrada com {} termos mostrados !'.format(termo))

'''for c in range(0, c):
    print('{} -> '.format(termo), end='')
    termo += n2
    contador += 1'''
