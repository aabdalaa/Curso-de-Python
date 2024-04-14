from random import randint
print('=-' * 16)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 16)
c = 0
while True:
    computador = randint(0, 11)
    n = int(input('Diga um valor: '))
    opcao = input('Par ou ímpar? [P/I] ').strip()[0]
    soma = computador + n
    while opcao not in 'PpIi':
        opcao = input('Par ou ímpar? [P/I] ').lower()
    print('-' * 30)
    if soma % 2 == 0 and opcao in 'p' or soma % 2 != 0 and opcao in 'i':
        c += 1
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} ', end='')
        print('DEU PAR.' if soma % 2 == 0 else 'DEU ÍMPAR')
        print('-' * 30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 16)
    elif soma % 2 != 0 and opcao in 'p' or soma % 2 == 0 and opcao in 'i':
        print(f'Você jogou {n} e o computador {computador}. Total de {soma} ', end='')
        print('DEU PAR.' if soma % 2 == 0 else 'DEU ÍMPAR')
        break
print('Você PERDEU!')
print('=-' * 16)
print(f'GAME OVER! Você venceu {c} vezes.')
