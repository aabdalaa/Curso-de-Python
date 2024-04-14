frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
print('você digitou a frase {}.'.format(juntar))
inverso = ''
for m in range(len(juntar) - 1, - 1, - 1):
    inverso += juntar[m]
print('o inverso de {} é {}.'.format(juntar, inverso))
if inverso == juntar:
    print('temos um polindromo ! ')
else:
    print('a frase que você digitou não é um políndromo !')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
''' outro jeito de fazer '''
'''inverso = juntar[::-1]'''
'''e tirar as linhas 5, 6 e 7 '''
