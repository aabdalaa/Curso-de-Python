from math import factorial
print('---'*20)
s = int(input('Digite seu fatorial: '))
print('---'*20)

def fatorial():
    for c in range(1, s):
        print(f'. {c}', end=' ')
    print(f'. {s}', end=' = ')



fatorial()
print(factorial(s))
print('---'*20)