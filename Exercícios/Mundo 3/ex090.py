lol = dict()
nomes = str(input('Nome: '))
medias = float(input(f'Média de {nomes}: '))
lol["nome"] = nomes
lol["media"] = medias
print('-=-'*20)
print(f'- O nome do aluno é: {nomes}')
print(f'- A média do aluno foi: {medias}')
if medias <= 3:
    print('- Situação: Reprovado !')
elif 5.9 >= medias > 3:
    print('- Situação: Recuperação !')
else:
    print('- Situação: Parabéns, aluno Aprovado !')
