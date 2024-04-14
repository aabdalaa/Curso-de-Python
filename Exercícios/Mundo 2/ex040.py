n1 = float(input('digite a primeira nota do aluno: '))
n2 = float(input('digite a segunda nota do aluno: '))
n3 = float(input('digite a terceira nota do aluno: '))
n4 = float(input('digite a quarta nota do aluno: '))
n5 = (n1+n2+n3+n4) / 4
if n5 < 5:
    print('O aluno foi reprovado.')
elif 7 > n5 >= 5:
    print('As notas {}, {}, {}, {} deixam a média do aluno: {}'.format(n1, n2, n3, n4, n5))
    print('O aluno está de recuperção ! Estude mais na próxima !')
elif n5 >= 7:
    print('As notas {}, {}, {}, {} deixam a média do aluno: {}'.format(n1, n2, n3, n4, n5))
    print('Parabéns o aluno não ficou de recuperção !!! ')
