par = list()
lista = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    print('-=-'*20)
    n1 = str(input('Deseja continuar [S/N]? ')).upper()
    print('-=-'*20)
    if n1 == 'S':
        continue
    if n1 == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {par}')
print(f'A lista de números impares é {impar}')
