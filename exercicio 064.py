#Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números 
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).
s = 0
n = 0 #int(input('Entre com o número inteiro: '))
cont = 0
n = int(input('Digite um número:  \033[1;34m [PARA PARAR O PROGRAMA DIGITE 999] \033[m'))
#colocando o n emcima ele acaba ignorando o 999 e assim podendo fazer a operação normal abaixo
while n != 999:
    cont+=1
    s += n 
    #t = s - 999
    n = int(input('Digite um número:  \033[1;34m [PARA PARAR O PROGRAMA DIGITE 999] \033[m'))

print('Foram digitados {} números e a soma entre eles é {}'.format(cont,s))
print('FIM')
