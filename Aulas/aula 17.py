"""print('-=-=-=-=-=-=-=- cardápio =-=-=-=-=-=-=-')
print('-=-'*13)
lanche = ('Big Mac', 'Duplo Big Mac', 'Duplo Quarterão', 'Big Tasty',
          'Big Tasty Turbo Queijo', 'Picanha Club House', 'McPicanha', 'McChicken', 'McChicken Bacon',
          'ClubHouse Chicken Crispy', 'Cheddar McMelt', 'Duplo Cheddar', 'Quarterão', 'McNífico Bacon',
          'Duplo Barbecue', 'Cheeseburger', 'Hamburger', 'Duplo Salada', 'McDuplo', 'McFiesta')
pyong = ''
alek = 0
print('''[0]Big Mac
[1]Duplo Big Mac
[2]Duplo Quarterão
[3]Big Tasty
[4]Big Tasty Turbo Queijo
[5]Picanha Club House
[6]McPicanha
[7]McChicken
[8]McChicken Bacon
[9]ClubHouse Chicken Crispy
[10]Cheddar McMelt
[11]Duplo Cheddar
[12]Quarterão
[13]McNífico Bacon
[14]Duplo Barbecue
[15]Cheeseburger
[16]Hamburger
[17]Duplo Salada
[18]McDuplo
[19]McFiesta''')
cont = str(input('vamos começar [S/N] ? ')).upper()
while cont == 'S':
    opcao = int(input(f'Digite o lanche desejados: '))
    print(f'O lanche escolhido foi {lanche[opcao]}')
    coot = str(input('deseja continuar [S/N]: ')).upper()
    if cont == 'N':
        break
    if coot == 'N':
        print(f'Obrigado por comprar no Macdonald, tenha um bom Macdia !')
        break"""
