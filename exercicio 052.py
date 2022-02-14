#Faça um programa que leia um número inteiro e diga se ele é 
# ou não um número primo.
tot = 0
num = int(input('Digite um numero: '))
for c in range(1,num + 1):
    
    if num % c == 0:
        print('\033[34m',end=' ') #se for divisivel
        tot += 1 # tot = tot + 1
    else:
        print('\033[31m',end=' ') #se não for divisivel
    print('{}'.format (c),end=' ')
print('\nO número {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('É por isso que ele é PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')