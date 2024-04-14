from uteis import mathesolution

def dinheiro(n, moeda='R$ '):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def fatorial(n, falso=False):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f if falso is False else dinheiro(n)

def dobro(n, falso=False):
    return n * 2 if falso is False else dinheiro(n)

def triplo(n, falso=False):
    return n * 3 if falso is False else dinheiro(n)

def metade(n, falso=False):
    return n/2 if falso is False else dinheiro(n)

def aumentoporcentagem(n, taxa, falso=False):
    q = n + (n * taxa/100)
    return q if falso is False else dinheiro(n)

def diminuirporcentagem(n, taxa, falso=False):
    return n - (n * taxa/100) if falso is False else dinheiro(n)

def tabela(h, n, y, o):
    p = n / 2
    x = n * 2
    q = n + (n * y/100)
    m = n - (n * o/100)
    print('___' * 10)
    print(f'{h.center(30)}')
    print('___' * 10)
    print(f'Preço analisado:   \t{mathesolution.moeda(n)}')
    print(f'Dobro do preço:    \t{mathesolution.moeda(x)}')
    print(f'Metade do preço:   \t{mathesolution.moeda(p)}')
    print(f'{y}% de aumento:   \t{mathesolution.moeda(q)}')
    return f'{o}% de redução:  \t{mathesolution.moeda(m)}'
    print('___' * 10)

def virgula(msg):
    valido = False
    while not valido:
        n = str(input(msg)).replace(',', '.')
        if n.isalpha() or n.strip() == '':
            print(F'\033[0;31mERRO: {n} É INVÁLIDO COMO PREÇO !\033[m')
        else:
            valido = True
            return float(n)

def tabel(n, y, o, h='RESUMO DO VALOR',):
    p = n / 2
    x = n * 2
    q = n + (n * y/100)
    m = n - (n * o/100)
    print('___' * 10)
    print(f'{h.center(30)}')
    print('___' * 10)
    print(f'Preço analisado:   \t{mathesolution.moeda(n)}')
    print(f'Dobro do preço:    \t{mathesolution.moeda(x)}')
    print(f'Metade do preço:   \t{mathesolution.moeda(p)}')
    print(f'{y}% de aumento:   \t{mathesolution.moeda(q)}')
    return f'{o}% de redução:  \t{mathesolution.moeda(m)}'
    print('___' * 10)

def km(n):
    p = n/1000
    return f'{p:.3f}'
