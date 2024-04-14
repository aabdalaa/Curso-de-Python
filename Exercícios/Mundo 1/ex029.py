km = float(input('A quantos KM/H seu carro andou ? '))
if km < 111:
    print('tenha um bom dia e dirija com segurança')
else:
    multa = (km - 110) * 7
    print('MULTADO!!! ')
    print('Tome mais cuidado, você ultrapassou o limite de velocidade, o valor da multa é de: R$ {:.2f}'.format(multa))
    print('tenha um bom dia e dirija com segurança ! ')
