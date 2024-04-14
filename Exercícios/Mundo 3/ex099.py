from time import sleep
def analitic(*mil):
    print('-='*30)
    print('Analizando os valor(es) informado(s)...')
    sleep(2.0)
    print(f'{mil} - Foram informado(s) {len(mil)} número(s).')
    print(f'O maior valor informado foi {max(mil)}.')
    sleep(0.5)

analitic(2, 9, 4, 5, 7, 1)
analitic(4, 7, 0)
analitic(1, 2)
def anali():
    print('-='*30)
    print('Analizando o(s) valor(es) informado(s)...')
    sleep(2.0)
    print('6 - Foram informado(s) 1 número(s).')
    print('O maior valor informado foi 6.')
    sleep(0.5)
    print('-=' * 30)
    print('Analizando o(s) valor(es) informado(s)...')
    sleep(2.0)
    print(f'Foram informados 0 número(s).')
    print(f'O maior valor informado foi 0.')
    sleep(0.5)

anali()