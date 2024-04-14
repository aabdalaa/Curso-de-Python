print('QUANDO FOR ESCREVER SUBSTITUA A VIRGULA POR PONTO.')

n1 = float(input('qual é o seu peso ? (kg): '))
n2 = float(input('qual a sua altura ? (m): '))
n3 = n1 / (n2 ** 2)
print('O seu Índice de massa corporal (IMC) é de {:.1f}'.format(n3))
if n3 < 18.5:
    print('você está ABAIXO DO PESO IDEAL ! ')
elif 18.5 <= n3 < 25:
    print('você está no PESO IDEAL.')
elif 25 <= n3 < 30:
    print('você está em SOBREPESO.')
elif 30 <= n3 < 40:
    print('você está em OBESIDADE, cuidado !')
elif n3 >= 40:
    print('você está em OBESIDADE MÓRBIDA !')
