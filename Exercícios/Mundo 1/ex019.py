import random
n1 = str(input('digite o nome do primeiro aluno: '))
n2 = str(input('digite o nome do segundo aluno: '))
n3 = str(input('digite o nome do terceiro aluno: '))
n4 = str(input('digite o nome do quarto aluno: '))
lista = (n1, n2, n3, n4)
h = random.choice(lista)
print(f'o aluno escolhido foi: {h}. ')
