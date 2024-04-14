def menu(n='MENU PRINCIPAL'):
    print('___'*15)
    print(n.center(43))
    print('___'*15)

def escolha(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print('___' * 15)
    try:
        opc = int(input('\033[32mSua opção: \033[m'))
        return opc
    except (ValueError, TypeError, KeyboardInterrupt):
        print('___' * 15)
        print('\033[31mOcorreu um erro, Tente novamente !\033[m ')
