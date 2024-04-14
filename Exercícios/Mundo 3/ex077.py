lista = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', \
        'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
for c in lista:
    print(f'\nNa palavra {c} temos a vogal: ', end='')
    for lista in c:
        if lista.lower() in 'aeiou':
            print(lista, end=' ')
