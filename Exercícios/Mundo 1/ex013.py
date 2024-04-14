n1 = float(input('digite o seu salário atual: R$'))
n2 = int(input('digite o aumento que você recebeu: %'))
n3 = n1+(n1*n2/100)
print('sua remuneração de {}% te dara um salário de R${:.2f}.'.format(n2, n3))
