from time import sleep
lista = list()
while True:
    dem = str(input('NOME: ')).upper()
    print('-'*28)
    not1 = float(input('NOTA 1: '))
    print('-'*28)
    not2 = float(input('NOTA 2: '))
    print('-'*28)
    amrt = (not1 + not2) / 2
    lista.append([dem, [not1, not2], amrt])
    cont = str(input('Deseja continuar [S/N]? ')).upper()
    print('-'*28)
    if cont == 'S':
        continue
    if cont == 'N':
        break
print(f'{"Nº:":<10}{"NOME:":<10}{"MÉDIA:":>8}')
print('-'*28)
for i, a in enumerate(lista):
    print(f'{i:<10}{a[0]:<10}{a[2]:>8}')
    print('-'*28)
while True:
    mst = int(input('Mostrar a nota de qual aluno (para finalizar digite 999)? '))
    if mst == 999:
        print('FINALIZANDO...')
        sleep(2)
        break
    else:
        print(f'As notas do aluno ({lista[mst][0]}) são: {lista[mst][1]}')
        continue
