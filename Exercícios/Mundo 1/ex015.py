dias = int(input('´Por quantos dias foi alugado ? '))
Km = int(float(input('quantos Km rodados ? Km ')))
pago = (dias*60) + (Km*0.15)
print('o total a pagar é de R${:.2f}.'.format(pago))
