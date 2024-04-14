def aumentar(preco, aumento, show=False):
    preco = preco + (preco * aumento) / 100

    if show:
        return moeda(preco)
    else:
        return preco


def diminuir(preco, reducao, show=False):
    preco = preco - (preco * reducao) / 100

    if show:
        return moeda(preco)
    else:
        return preco


def dobro(preco, show=False):
    preco *= 2

    if show:
        return moeda(preco)
    else:
        return preco


def metade(preco, show=False):
    preco /= 2

    if show:
        return moeda(preco)
    else:
        return preco


def moeda(preco):
    return f'R$ {preco:.2f}'.replace('.', ',')
