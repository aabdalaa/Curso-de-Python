num: int = 0
while True:
    print('-=-' * 20)
    num = int(input('DIGTE UM NÚMERO PARA SABER SUA TABUADA: '))
    print('-=-' * 20)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {c * num}')

print('o programa acabou, volte sempre !')
