frase = str(input('digite uma frase: ')).lower().strip()
print('a letra ''a'', apareceu {} em sua frase'.format(frase.count('a')))
print('a primeira letra ''a'', apareceu na posição {}.'.format(frase.find('a')+1))
print('a última letra ''a'', aparece na posição {}.'.format(frase.rfind('a')+1))
' rfind procura uma letra, frase, sinal ou números do final da frase para o começo '
