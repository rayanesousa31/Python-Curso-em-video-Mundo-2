#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Digit eum número inteiro: '))

print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADOMINAL é {}'.format(num,hex(num)[2:]))
else : #elif opção >3:
    print('Opção inválida. Tente novamente.')