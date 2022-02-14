#Faça um programa que calcule a soma entre todos os numeros impares que são 
#múltiplos de 3 e que se encontram no intervalo de 1 a 500.

soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0: 
        print(c,end=' ')
        soma += c
        cont += 1
print('\nA soma de todos os números multiplos de 3 é de {} e a quantidade de números é {}'.format(soma, cont))
        


#---------------------RESOLUÇÃO GUANABARA

soma = 0
cont = 0
for num in range (1, 501,2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
        print(num, end=' ')
print('A soma dos {} valores é {}'.format(cont,soma))
