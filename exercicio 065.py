#Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e o menor 
# valores lidos.# O programa deve perguntar ao usuário se 
# ele quer ou não continuar a digitar valores.

t=0
opção = 'S'
cont = 0
med = 0
while opção == 'S':
    n = int(input('Digite o número:'))
    t += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opção = str(input('Gostaria de digitar mais valores?[S/N] ')).upper().strip()
med = t / cont

print('A média dos valores digitados é {}, o maior valor foi {} e o menor valor {}'.format(med,maior,menor))