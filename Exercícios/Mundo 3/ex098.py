"""from time import sleep
def linha50():
    print('-=-'*20)
def linha(dev):
    linha50()
    print(dev)
    for s in range(1, 11, 1):
        print(s, end=' ')
        sleep(0.5)
    print('FIM !')

linha('contagem de 1 até 10 de 1 em 1.')

def linha1(dev2):
    linha50()
    print(dev2)
    linha50()
    for k in range(0, 11, 2):
        print(k, end=' ')
        sleep(0.5)
    print('FIM !')

linha1('Contagem de 0 até 10 de 2 em 2.')
linha50()
print('Agora sua vez !')
linha50()
ini = int(input('INÍCIO: '))
fim = int(input('FIM:    '))
pas = int(input('PASSO:  '))
linha50()
print(f'contagem de {ini} até {fim} de {pas} em {pas}')
linha50()
for c in range(fim,ini+1, pas):
    if pas < 0:
        pas *= -1
    print(c, end=' ')
print('FIM !')"""

from time import sleep


def cont(x, y, z):
    for c in range(x, y, z):
        sleep(0.5)
        print(f'{c}..', end='')
    print('FIM')
    print('--' * 30)


def ver(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('Contando de {} ate {} (de {} em {})'.format(a, b, c, c))
    if a > b:
        b -= 1
        if c > 0:
            c *= -1
    elif a < b:
        b += 1
        if c < 0:
            c -= 1
    cont(a, b, c)


def linha(x):
    print('-' * (len(x) + 1))
    print('{}'.format(x))
    print('-' * (len(x) + 1))


# Programa Principal
linha('CONTADOR INTELIGENTE')
ver(1, 10, 1)
ver(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ver(int(input('Quer começar de qual número: ')), int(input('Quer ir até qual número: ')),
    int(input('Qual o valor do passo: ')))