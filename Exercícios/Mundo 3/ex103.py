print('___'*20)
s = input('Qual o nome do jogador ? ')
t = input('Quantos gols ele(a) fez ? ')
def sol(a='<DESCONHECIDO>', b=0):
    if s == '':
        print(F'O JOGADOR ', end='')
        print(a, end=' ')
        print('FEZ ', end='')
        print(t, end=' ')
        print('GOLS NO CAMPEONATO.')
    elif t == 0:
        print('___' * 20)
        print(F'O JOGADOR ', end='')
        print(s, end=' ')
        print('FEZ ', end='')
        print(b, end=' ')
        print('GOLS NO CAMPEONATO.')
    else:
        print(F'O JOGADOR {s} FEZ {t} GOLS NO CAMPEONATO.')


print('___'*20)
sol()
