#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#A média de idade do grupo
#Qual o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaid = 0
med = 0
maioridh = 0
nomevelho = ' '
mulher20 = 0
for p in range (1,5):
    print ('~~~~~~~~ PESSOA {} ~~~~~~~~'.format(p))
    nome = str(input('Digite seu nome:'))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('''Qual o seu sexo: 
    [1] MASCULINO
    [2] FEMININO
    '''))
    somaid += idade
    if p ==1 and sexo == 1:
        maioridh = idade
        nomevelho = nome
    if sexo == 1  and idade > maioridh:
        maioridh = idade
        nomevelho = nome 
    if sexo == 2 and idade < 20:
        mulher20 += 1    
med = somaid / 4
print('A média da idade do grupo é de  {}'.format(med)) 
print('O nome do homem mais velho é {}'.format(nomevelho))
print('A quantidade de mulher que tem menos de 20 anos é {}'.format(mulher20))