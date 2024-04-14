from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    b = int(input('Em que ano a {}° pessoa nasceu ? '.format(c)))
    v = date.today().year - b
    print('essa pessoa tem {} anos de idade !'.format(v))
    if v >= 18:
        print('essa pessoa já é maior de idade !')
        totmaior += 1
    elif v <= 17:
        print('essa pessoa ainda é menor de idade !')
        totmenor += 1
    print('-=-'*20)
print('essas idades citadas seriam {} maior(es) de idade e'.format(totmaior))
print('{} menor(es) de idade !'.format(totmenor))
