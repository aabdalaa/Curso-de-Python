'''example = list()
example.append('André Luiz')
example.append(14)
print(example)
print(example[0])
print(example[1])
galera = list()
galera.append(example[:])
example[0] = 'maria'
example[1] = 34
galera.append(example[:])
print(galera)'''

'''galera = [['andré', 14], ['luiz', 14], ['gustavo', 40], ['maria', 34]]
print(galera)
print('-=-'*20)
print(galera[0])
print('-=-'*20)
print(galera[1])
print('-=-'*20)
print(galera[2])
print('-=-'*20)
print(galera[3])
print('-=-'*20)
print(galera[0][0], end=', ')
print(galera[2][1])
print('-=-'*20)
for c in galera:
    print(f'{c[0]} tem {c[1]} anos de idade')'''

"""galera = list()
dados = list()
maior = 0
menor = 0
for c in range(0, 3):
    dados.append(str(input('NOME: ')))
    dados.append(int(input('IDADE: ')))
    print('-=-'*20)
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Na lista tem {maior} maiores de idade, e {menor} menores de idade !')"""
