from uteis import mathesolution
from uteis import matematica

s = float(input('Digite o preço: R$ '))
print('___'*20)
print(f'A metade de {matematica.dinheiro(s)} é: {mathesolution.metade(s, True)}')
print('___'*20)
print(f'O dobro de {matematica.dinheiro(s)} é: {mathesolution.dobro(s, True)}')
print('___'*20)
print(f'Um aumento de 10% no valor {matematica.dinheiro(s)} é igual a: {mathesolution.aumentar(s, 10, True)}')
print('___'*20)
print(f'Uma diminuição de 10% no valor {matematica.dinheiro(s)} é igual a: {mathesolution.diminuir(s, 10, True)}')
