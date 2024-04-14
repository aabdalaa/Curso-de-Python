'''print('==='*20)
print('ACEITAMOS SOMENTE VALORES INTEIROS !!!')
print('==='*20)
print('BANCO DO VIVALDI')
print('==='*20)
n1 = int(input('QUE VALOR DESEJA SACAR ? R$ '))
n2 = n1
ced = 50
totced = 0
while True:
    if n2 >= ced:
        n2 -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if n2 == 0:
            break
print('==='*20)
print('AGRADECEMOS A PREFERÊNCIA, TENHA UM BOM DIA !!!')
print('==='*20)'''
