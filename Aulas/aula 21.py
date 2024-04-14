"""def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

print('---'*20)
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')"""

def parouimpar(n=0):
    """

    :param n: isso é uma docstring
    :return:
    """
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if parouimpar(num):
    print('É um número par')
else:
    print('É um número impar')
