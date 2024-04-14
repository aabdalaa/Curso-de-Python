sexo = str(input('digite seu sexo MASCULINO[M/F]FEMINO: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo inválido ! digite seu sexo novamente: ')).upper().strip()[0]
print('sexo {} contabilizado ! obrigado !'.format(sexo))
