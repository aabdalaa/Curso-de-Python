c = 0
b = 0
h = 0
while b <= 998:
    b = int(input('digite um número [999 para parar de executar]: '))
    c += b
    h += 1
if b == 999:
    c -= 999
    h -= 1
print('Vôce digitou {} números e a soma dos números é igual a {} !'.format(h, c))
