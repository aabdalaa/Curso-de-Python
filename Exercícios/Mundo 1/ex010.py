from uteis import matematica

din = matematica.virgula('quanto dinheiro você tem na sua carteira R$: ')

print(f'Com R$ {matematica.dinheiro(din)} você pode comprar U$ {matematica.dinheiro(din/5.31)}')
