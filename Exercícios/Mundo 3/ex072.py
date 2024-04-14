num1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num2 = int(input('digite um número de 0 a 20: '))
    if 0 <= num2 <= 20:
        break
    print('TENTE NOVAMENTE. ', end='')
print(f'você digitou o número {num1[num2]} !')
