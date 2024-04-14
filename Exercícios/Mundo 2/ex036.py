casa = float(input("Qual é o valor da casa ? R$ "))
salario = float(input("Qual é o valor do seu sálario ? R$ "))
tempo = int(input('por quantos anos você deseja pagar ? '))
prestacao = casa / (tempo * 12)
minimo = salario * (30 / 100)
print('para pagar uma casa de R${:.2f} em {} anos '.format(casa, tempo), end='')
print('o valor necessário para a prestação será de: R${:.2f}.'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo PODE SER CONCEDIDO !')
else:
    print('Emprestimo NEGADO !')
