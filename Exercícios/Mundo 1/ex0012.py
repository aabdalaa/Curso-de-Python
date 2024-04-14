n1 = float(input('digite um valor de um produto: R$ '))
n2 = float(input('digite o desconto do produto: % '))
s = n1-(n1*n2/100)
print('o valor do seu produto R${:.2f} com {:.2f}% de desconto é R${:.2f}'.format(n1, n2, s))
