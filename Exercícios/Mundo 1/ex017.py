'''n1 = float(input('digite o comprimento do cateto oposto : '))
n2 = float(input('digite o comprimento do cateto adjecente: '))
n3 = (n1 ** 2 + n2 ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(n3))'''

from math import hypot
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('o valor da hipotenusa é {:.2f}'.format(hi))
