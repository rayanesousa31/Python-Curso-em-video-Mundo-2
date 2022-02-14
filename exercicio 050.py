#Desenvolva um programa que leia seis números inteiros e mostre 
# a soma apenas daqueles que forem pares. Se o valor digitado for
#impar, desconsidere-o.

soma = 0
cont = 0
for num in range (1,7):
    n = int(input('Digite o {}º numero: '.format(num)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos valores pares digitados são {} e sua quantidade são {}'.format(soma,cont))


   