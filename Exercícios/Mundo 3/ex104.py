h = 0
def num():
    while True:
        print('___'*20)
        g = input('DIGITE UM NÚMERO: ').strip()
        print('___'*20)
        if g.isnumeric():
            print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO {g} !')
        else:
            print('\033[0;31mOCORREU UM ERRO, TENTE NOVAMENTE !\033[m')


num()
