while True:
    try:
        print('___'*20)
        s = int(input('Digite um número inteiro: '))
        print('---'*20)
        n = float(input('Digite um número real: '))
        print('---'*20)
        print(f'O valor inteiro foi {s} e o valor real foi {n}')
        break
    except (ValueError, TypeError, KeyboardInterrupt):
        print('___' * 20)
        print('\033[31mOcorreu um erro, tente novamente !\033[m ')
