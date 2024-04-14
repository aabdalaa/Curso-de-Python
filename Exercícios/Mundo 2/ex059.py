from time import sleep
m = 0
v = 0
maio = 0
o = 0
print('coloque o ''.'' para números como: 2.2, 3.7, 9.8 !')
print('-=-'*20)
p = float(input('digite o primeiro valor: '))
s = float(input('digite o segundo valor: '))
while o != 5:
    print('''    [ 1 ] somar    
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    o = int(input('>>>>> digite uma opção: '))
    if o == 1:
        m = p + s
        print('o resultado de {} + {} é igual a {} !'.format(p, s, m))
    elif o == 2:
        v = p * s
        print('os números {} * {} multiplicados são iguais a {} !'.format(p, s, v))
    elif o == 3:
        if p > s:
            print('entre os números {} e {} o maior é {}'.format(p, s, p))
        else:
            print('entre {} e {} o maior número é {}'.format(p, s, s))
    elif o == 4:
        p = float(input('digite o primero valor novamente : '))
        s = float(input('digite o segundo valor novamente: '))
    elif o == 5:
        print('finalizando ...')

    else:
        print('houve um erro em seu programa tente novamente !')
    print('-=-'*20)
    sleep(1)
print('fim do programa ! volte sempre ! :)')
