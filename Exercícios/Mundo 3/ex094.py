"""dicio = dict()
lis = list()
M = 0
F = 0
p = 0
i = 0
while True:
    dicio.clear()
    p += 1
    dicio["nome"] = str(input('Nome: '))
    print('---'*20)
    dicio["sexo"] = str(input('SEXO[M/F]: ')).upper()
    if dicio["sexo"] == 'M':
        M += 1
    if dicio["sexo"] == 'F':
        F += 1
    if dicio["sexo"] not in 'MF':
        print('ERRO! TENTE NOVAMENTE !')
        print('---'*20)
        continu = str(input('SEXO[M/F]: ')).upper()

    print('---'*20)
    dicio["idade"] = int(input('Idade: '))
    lis.append(dicio.copy)
    i += dicio["idade"]
    print('---'*20)
    continuar = str(input('Deseja continuar[S/N]? ')).upper()
    print('---'*20)
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
    else:
        print('ERRO ! TENTE NOVMENTE')
        print('---'*20)
        continuar = str(input('Deseja continuar[S/N]? ')).upper()
        print('---'*20)

print(f'A) Ao todo temos {p} pessoas cadastradas.')
print(f'B) A média de idade dessas pessoas é de {i/p} anos.')
print(f'C) {dicio.items()}')"""

pessoas = dict()
chavenomes = list()
chaveidades = list()
chavesexo = list()
mulheres = list()
continuar = ' '


while True:
    nome = str(input('Nome: '))
    chavenomes.append(nome)
    pessoas['nome'] = chavenomes

    print('---'*20)


    sexo = str(input('Sexo: M/F: ')).upper()
    print('---'*20)
    if sexo not in 'MF':
        print('erro')
        chavenomes.pop()
        continue
        print('---'*20)

    elif sexo in 'FM':
        chavesexo.append(sexo)
        pessoas['sexo'] = chavesexo


    idade = int(input('Idade: '))
    chaveidades.append(idade)
    pessoas['idade'] = chaveidades
    print('---'*20)


    continuar = str(input('Continuar? S/N: '))
    if continuar in 'nN':
        break
    print('-=-'*20)

for nome, sexo, idade in zip(chavenomes, chavesexo, chaveidades):
    if sexo in 'F':
        mulheres.append(nome)


print('-=-' * 20)
print(f'A) Ao todo temos {len(chavenomes)} pessoas cadastradas.')
media = sum(chaveidades) / len(chaveidades)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print(f'D) Lista das pessoas que estão acima da média:')
for n, s, i in zip(chavenomes, chavesexo, chaveidades):
    if i > media:
        print(f'(maNome: = {n}; sexo = {s}; idade = {i};)')
