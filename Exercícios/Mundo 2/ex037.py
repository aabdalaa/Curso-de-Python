lol = int(input('digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal 
[ 3 ] Converter para Hexadecimal''')

opcao = int(input('digite uma opção para faze a conversação: '))

if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(lol, bin(lol)).lower())

elif opcao == 'binario':
    print('{} convertido para Binário é igual a {}'.format(lol, bin(lol)).lower())

elif opcao == 'binário':
    print('{} convertido para Binário é igual a {}'.format(lol, bin(lol)).lower())

elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(lol, oct(lol)).lower())

elif opcao == 'octal':
    print('{} convertido para Octal é igual a {}'.format(lol, oct(lol)).lower())

elif 3 == opcao:
    print('{} convertido para Hexadecimal é igual a {}'.format(lol, hex(lol)).lower())

elif opcao == 'hexadecimal':
    print('{} convertido para Hexadecimal é igual a {}'.format(lol, hex(lol)).lower())

else:
    print('um erro foi encontrado digite novamente.'.upper())