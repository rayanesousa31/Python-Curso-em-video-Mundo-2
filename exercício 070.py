#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar.
#No final mostre:
#Qual é o total gasto na compra
#Quantos produtos custam mais que 1000.00
#Qual é o nome do produto mais barato

barato = ' '
total = totalmil =  0
cont = menor = 0
while True:
    prod = str(input('Nome do produto: ')).upper().split()
    preco = float(input('Quanto o produto custa? R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totalmil += 1
    if cont == 1:        #se o contador for igual a 1 , ou seja, se for o primeiro valor aser digitado
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    resp= ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]')).upper().split()[0]
    if resp == 'N':
        break

print(f'O valor do produtomais barato é {menor} e é {barato}. O total da compra foi R${total}')
print(f'A quantidade de produtos que custam acima de 1000.00 é {totalmil} intens')

