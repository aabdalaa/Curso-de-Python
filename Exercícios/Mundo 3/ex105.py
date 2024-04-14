def resp():
    """
    a = notas.
    h = soma as notas e divide elas.
    k = a quantidade de notas presentes.
    dicio = dicionário python
    """
    print('___'*20)
    a = (6, 6, 6, 6)
    h = 0
    k = 0
    for _ in a:
        k += 1
    h += sum(a) / k
    if h >= 6:
        pol = 'boa'
    else:
        pol = 'ruim'
    dicio = {"total": k, "maior": max(a), "menor": min(a), "media": h, "situação": pol}
    print(dicio)
    print('___' * 20)
resp()
help(resp)
