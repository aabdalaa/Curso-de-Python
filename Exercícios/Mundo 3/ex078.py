lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-=-'*20)
print(f'Os números digitados foram: {lista}')
print('---'*20)
print(f'O menor valor foi o número {min(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
print()
print(f'O maior valor foi o número {max(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
