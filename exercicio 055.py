#Faça um programa que leia o peso de 5 pessoas.
#No final, mostre qual foi o maior e o menor 
# peso lidos.
pesomaior = 0
pesomenor = 0

for pessoa in range (1,6):
    peso = float(input('Peso da {} pessoa: '.format(pessoa)))

    if pessoa == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi {}KG'.format(pesomaior))
print('O menor peso lido foi de {}KG'.format(pesomenor))




