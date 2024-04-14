from time import sleep
import urllib.request
import webbrowser

while True:
    try:
        urllib.request.urlopen("http://www.pudim.com.br")
    except Exception as erro:  # Desligando o wifi, ou o site não estiver no ar
        print('---'*20)
        print('\033[1; 31mO site Pudim não está acessível no momento.\033[m')
        er = erro  # Variável usada para não ter marcações de erro no código pelo PyCharm.
    else:  # Com wifi ligado:
        print('---'*20)
        print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')