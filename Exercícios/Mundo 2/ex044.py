print(f'{" LOJAS ABDALA ":=^40}')
preco = float(input('preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] Á vista (dinheiro ou cheque)
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('qual é a opção ? '))
if opcao == 1:
    total1 = preco - (preco * 10/100)
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total1))
elif opcao == 2:
    total2 = preco - (preco * 5/100)
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total2))
elif opcao == 3:
    total = preco
    parcela = (total / 2)
    print('sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 4:
    total3 = preco + (preco * 20/100)
    parcelatotal = int(input('quantos meses deseja parcelar: '))
    parcela2 = total3 / parcelatotal
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total3))
    print('sua compra será parcelada em {}x de R${} COM JUROS'.format(parcelatotal, parcela2))
else:
    print('opção invalida escreva novamente.')
