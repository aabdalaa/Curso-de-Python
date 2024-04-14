n1 = int(input('digite um valor:'))
n2 = int(input('digite outro valor:'))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
print('a soma é {} , a multiplicação é {} , a divisão é {} , subtração é {} , '.format(a, m, d, s), end='')
print('divisão inteira {} e a potência {}.'.format(di, p))
