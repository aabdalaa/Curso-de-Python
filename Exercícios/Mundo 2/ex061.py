print('10 TERMOS DE UMA P.A')
print('-=-'*20)
n1 = int(input('digite o primeiro termo: '))
n2 = int(input('digite a razão: '))
termo = n1
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += n2
    contador += 1
print('FIM !')
