num = int(input('DIGTE UM NÚMERO PARA SABER SUA TABUADA: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
