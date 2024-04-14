from math import factorial
n = int(input('Digite um número para calcular seu FATORIAL: '))
f = factorial(n)
c = n
print('calculando {}! = o fatorial de {}! é igual a: {} '.format(n, n, f))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= 1
    c -= 1
print('{}'.format(f), end='')
