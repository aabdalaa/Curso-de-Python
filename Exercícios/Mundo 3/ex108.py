from uteis import matematica

s = float(input('Digite o preço: R$ '))
print('___'*20)
print(f'A metade de {matematica.dinheiro(s)} é: R$ {matematica.dinheiro(matematica.metade(s))}')
print('___'*20)
print(f'O dobro de {matematica.dinheiro(s)} é: R$ {matematica.dinheiro(matematica.dobro(s))}')
print('___'*20)
print(f'Um aumento de 10% no valor {matematica.dinheiro(s)} é igual a: R$ {matematica.dinheiro(matematica.aumentoporcentagem(s, 10))}')
print('___'*20)
print(f'Uma diminuição de 10% no valor {matematica.dinheiro(s)} é igual a: R$ {matematica.dinheiro(matematica.diminuirporcentagem(s, 10))}')
