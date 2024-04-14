from uteis import matematica

s = float(input('Digite o preço: R$ '))
print('___'*20)
print(f'A metade de R$ {s} é: R$ {matematica.metade(s)}')
print('___'*20)
print(f'O dobro de R$ {s} é: R$ {matematica.dobro(s)}')
print('___'*20)
print(f'Um aumento de 10% no valor R$ {s} é igual a: R$ {matematica.aumentoporcentagem(s, 10)}')
print('___'*20)
print(f'Uma diminuição de 10% no valor R$ {s} é igual a: R$ {matematica.diminuirporcentagem(s, 10)}')
