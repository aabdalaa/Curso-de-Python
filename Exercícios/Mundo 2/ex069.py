print('-=-'*20)
print('CADASTRE UMA PESSOA.')
print('-=-'*20)
n1 = 0
i = 0
n2 = ''
m = 0
f = 0
vinte = 0
while True:
    n1 = int(input('IDADE: '))
    if n1 >= 18:
        i += 1
    n2 = str(input('SEXO [M/F]: ')).strip().lower()
    if n2 == 'm':
        m += 1
    elif n2 == 'f':
        f += 1
        if n2 == 'f' and n1 <= 20:
            vinte += 1
    print('-=-'*20)
    n3 = str(input('DESEJA CONTINUAR [S/N]: ')).strip().lower()
    if n3 == 's':
        print('-=-'*20)
    elif n3 == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {i} ')
print(f'Ao todo temos {m} homens cadastrados !')
print(f'E temos {vinte} mulheres com menos de 20 anos !')
print('-=-'*20)
print('volte sempre !')
