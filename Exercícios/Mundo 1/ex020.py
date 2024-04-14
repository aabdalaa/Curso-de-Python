from random import shuffle
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
kol = [n1, n2, n3, n4]
shuffle(kol)
print('a ordem de apresentação será')
print(kol)