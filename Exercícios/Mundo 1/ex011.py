num1 = float(input('largura da parede:'))
num2 = float(input('altura da parede:'))
s = num1*num2
print('sua parede tem a dimensão de {} x {} e sua área é de {:.3f} m²'.format(num1, num2, s))
tinta = s/2
print('para pintar essa parede você precisa de {} Litros de tinta'.format(tinta))
