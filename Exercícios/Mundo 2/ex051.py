print('10 TERMOS DE UMA P.A')
print('-=-'*20)
n1 = int(input('digite o primeiro termo: '))
n2 = int(input('digite a razão: '))
decimo = n1 + (10 - 1) * n2
print('-=-'*20)
for c in range(n1, decimo + n2, n2):
    print('{}'.format(c), end=' -> ')
print('acabou !')
