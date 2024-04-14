h = 0
n = 0
s = 0
while True:
    n = int(input('Digite um número [digite 999 para parar]: '))
    if n == 999:
        break
    s += n
    h += 1
print(f'A soma dos {h} valores é igual a {s} !')
