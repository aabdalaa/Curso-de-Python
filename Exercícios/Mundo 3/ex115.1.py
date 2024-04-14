from uteis import MENU, manipular
from time import sleep

arquivo = 'nome.txt'

if not manipular.abrir(arquivo):
    manipular.criar(arquivo)

while True:
    MENU.menu()
    resposta = MENU.escolha(['VER PESSOAS CADASTRADAS', 'CADASTRAR PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        print('___' * 15)
        print(manipular.ler(arquivo))
    if resposta == 2:
        print('___' * 15)
        print('OPÇÃO 1'.center(43))
    if resposta == 3:
        print('___'*15)
        print('SAINDO DO SISTEMA', end='')
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
