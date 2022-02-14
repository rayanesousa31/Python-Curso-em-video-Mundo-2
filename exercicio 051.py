#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final mostre os 10 prmeiros termos dessa progressão.

n = int(input('Digite um numero: '))
razao = int(input('Digite uma razao: '))
dec = n + (10-1) * razao 

for c in range (n, dec+razao, razao):
    print(c, end=' ')

