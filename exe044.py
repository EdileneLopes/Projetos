print( '{:-^40}'.format('LOJAS EDILENE'))
valor = float(input('Informe o preço da compra R$'))
print('''Opções de pagamento:
[1] À vista em Dinheiro
[2] À vista no cartão Débito
[3] Em 2x no Crédito
[4] Em 3x ou mais no Crédito''')
opção = int(input('Escolha uma das opções: '))
if opção == 1:
    total = valor - (valor * 10 / 100)
elif opção == 2:
    total = valor - (valor * 5 / 100)
elif opção == 3:
    total = valor
    parcela = (valor / 2)
    print('Sua compra será parcelada em 2x de R${:.2f}, e custará {:.2f} no final. SEM JUROS'.format(parcela, valor))
elif opção == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em \033[31m{}\033[mx, de \033[32mR${:.2f} \033[m COM JUROS.'.format(totparc, parcela))
else:
    total = valor
    print('\033[33mOPÇÃO INVÁLIDA de pagamento. Tente novamente\033[m')
print('Sua compra de R${:.2f} vai custar \033[33mR${:.2f}\033[m no final'.format(valor,total))
