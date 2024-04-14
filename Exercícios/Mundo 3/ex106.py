titulo = '\033[1;34mHelp Interactive'
print('\033[1;34m___'*20)
print(titulo.center(65))
while True:
    print('\033[1;34m___'*20)
    h = input('DIGITE UMA FUNÇÃO EM PYTHON PARA GANHAR AJUDA: ').lower().strip()
    print('___'*20)
    print()
    help(h)
    print('___'*20)
    print()
    d = str(input('Deseja continuar [s/n]: ')).lower()
    if d == 'n':
        break
    if d == 's':
        continue
