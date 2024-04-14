print('COLOQUE A LETRA M PARA MULHER E H PARA HOMEM !')
somaidade = 0
mediaidade = 0
homem = 0
nome = ''
mulheres = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    p = str(input('digite o nome da pessoa: ')).strip()
    k = int(input('digite a idade da pesssoa: '))
    s = str(input('digite o sexo da pessoa HOMEM[H/M]MULHER: ')).strip().lower()
    somaidade += k
    if c == 1 and s == 'h':
        homem = k
        nome = p
    if s == 'h' and k > homem:
        homem = k
        nome = p
    if s in 'm' and k >= 20:
        mulheres += 1
mediaidade = somaidade / 4
print('-=-'*20)
print('a média de idade do grupo é de {:.1f} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(homem, nome))
print('E o número de MULHERES acima dos 20 anos é de {} mulheres'.format(mulheres))
