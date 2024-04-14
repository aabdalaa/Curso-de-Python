n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
n4 = int(input('digite o quarto número: '))
fauna = (n1, n2, n3, n4)
print(f'Você digitou os valores {fauna}')
print('-=-'*20)
if 9 in fauna:
    print(f'o número nove apareceu {fauna.count(9)} vezes !')
else:
    print('o número nove não apareceu nenhuma vez')
print('-=-'*20)
if 3 in fauna:
    print(f'O número 3 apareceu na {fauna.index(3)+1}° posição !')
else:
    print('o valor 3 não apareceu em nenhuma posição !')
print('-=-'*20)
print('Os valores pares digitados foram: ')
for n in fauna:
    if n % 2 == 0:
        print(n)
print('-=-'*20)
