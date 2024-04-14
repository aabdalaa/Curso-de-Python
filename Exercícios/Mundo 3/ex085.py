listinha = [[], []]
valorante = 0
for c in range(1, 8):
    valorante = int(input(f'digite o {c}º valor: '))
    print('-=-'*20)
    if valorante % 2 == 0:
        listinha[0].append(valorante)
    else:
        listinha[1].append(valorante)
listinha[0].sort()
listinha[1].sort()
print(f'Os numeros pares são: {listinha[0]}')
print(f'Os números impares são: {listinha[1]}')
