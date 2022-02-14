#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e considerando
#de pagamento:
#a vista no dinheiro / cheque:10% de desconto
#a vista no cartao:5% de dessconto
#em qte 2x no cartao: preço normal
#3 x ou mais no cartão: 20% de juros

prod = float(input('O preço do produto é: R$'))
print('''Qual a forma de pagamento desejada? 
[1] DINHEIRO
[2] CHEQUE
[3] AVISTA NO CARTÃO
[4] CREDITO 2X
[5] CREDITO 3X OU MAIS''')
opção = int(input('Escolha uma das opções: '))


if opção == 1 :
    print('Pago em dinheiro no valor de R$ {}'.format(prod - (prod * 10/100)))
elif opção == 2:
    print('Pagamento em cheque fica no valor de R$ {}'.format(prod - (prod * 10/100)))
elif opção == 3:
    print('Pagamento a vista no cartão fica no valor de R$ {}'.format(prod - (prod * 5/100)))
elif opção == 4:
    print('Pagamento  no cartão em 2x fica no valor de R$ {}'.format(prod / 2))
elif opção == 5:
    qnt =  int(input('Quantidade de vezes em que gostaria de fazer o pagamento: '))
    print('Pago no cartão de crédito em {} vezes, ficará as parcelas no valor de R$ {}'.format(qnt, (prod + (prod * 20/100))/qnt))
else:
    print('Opção inválida. Por favor escolha outra opção')