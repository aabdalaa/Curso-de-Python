from uteis import MENU
from time import sleep

while True:
    MENU.menu()
    resposta = MENU.escolha(['VER PESSOAS CADASTRADAS', 'CADASTRAR PESSOAS', 'Sair do Sistema'])
    if resposta == 1:
        print('___'*15)
        print('OPÇÃO 1'.center(43))
        print('___' * 15)
    if resposta == 2:
        print('___' * 15)
        print('OPÇÃO 2'.center(43))
        print('___' * 15)
    if resposta == 3:
        print('___'*15)
        print('Saindo do sistema', end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        print('___'*15)
        break
    elif resposta > 3:
        print('\033[31mOcorreu um erro, Tente novamente !\033[m ')
