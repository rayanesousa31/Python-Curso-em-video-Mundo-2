#Refaça o DESAFIO 051,
# lendo o primeiro termo e a razão de uma PA, 
# mostrado os 10 primeiros termos da progressão 
# usando a estrutura while.

n = int(input('Digite um numero: '))
razao = int(input('Digite uma razao: '))

termo = n
cont = 1
while cont <= 10:
    print(' {}'.format(termo),end=' ')
    termo += razao
    cont+= 1
print('Fim')