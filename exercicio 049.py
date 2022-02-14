#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
#só que agora utilizando um laço for.

n = int(input('Escolha um número inteiro: '))

for c in range(1,11):
    res = n * c
    print('{} x {:2} = {}'.format(n,c,res))    #ou (n,c,n*c)