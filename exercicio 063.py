#Escreva um programa que leia um numero n inteiro 
# qualquer e mostre na tela os n primeiros elementos 
# de uma sequencia de fibonacci - : 1 + 2 = 3; 2 + 3 = 5; 3 + 5 = 8;


n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{} {}'.format(t1,t2),end='')
while cont <= n:
    t = t1 + t2
    print(' {}'.format(t),end='')
    t1 = t2
    t2 = t
    cont+=1
print(' fim')
