money = float(input('qual é o seu sálario atual ? R$').strip())
if money <= 1250:
    new = money + (money * 15/100)
else:
    new = money + (money * 10/100)
print('quem recebia R${:.2f} vai passar a receber R${:.2f}'.format(money, new))
