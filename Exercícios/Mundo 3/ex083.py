expressao = str(input('Digite uma expressão: '))
pilha = []
for sim in expressao:
    if sim == '(':
         pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta !')
else:
    print('Sua expressão está errada !')
