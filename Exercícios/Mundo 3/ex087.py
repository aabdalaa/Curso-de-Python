matrizes = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista = 0
kol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrizes[l][c] = int(input(f'Digite um valor para {[l], [c]}: '))
        print('---'*20)
print('OS VALORES EM MATRIZES SÃO:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrizes[l][c]:^5}]', end='')
        if matrizes[l][c] % 2 == 0:
            lista += matrizes[l][c]
        if 0 == 0:
            kol += matrizes[2][c]
    print()
print('---'*20)
print(f'a soma dos números pares é igual a: {lista}')
print('---'*20)
print(f'A soma da terceira coluna é igual a: ', end='')
print(f'{matrizes[0][2] + matrizes[1][2] + matrizes[2][2]}')
print('---'*20)
print(f'O maior valor da 2º linha é o: {max(matrizes[1])}')
