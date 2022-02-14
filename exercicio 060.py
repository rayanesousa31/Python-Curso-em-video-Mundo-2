#Faça um programa que leia um número qualquer e mostre
#o seu fatorial

import math
n = 1

while n != 0:
    n = int(input('Digite um número: '))
    fac = math.factorial(n)
    print('O fatorial do numero {} é {}'.format(n,fac))


#--------------------------- OUTRA FORMAR DE RESOLUÇÃO
n = int(input('Digite um número: '))
c =n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c),end='')
    print('x' if c > 1 else '=',end=' ')
    f *= c
    c-=1
print('{}'.format(f))