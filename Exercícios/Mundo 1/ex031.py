km = float(input('qual é a distância da sua viagem ? '))
print('você está prestes a começar uma viagem de {} Km !'.format(km))
if km <= 200:
    n1 = km * 0.50
else:
    n1 = km * 0.45
print('E o preço da sua viagem será R${:.2f}'.format(n1))
print('tenha uma ótima viagem !')
