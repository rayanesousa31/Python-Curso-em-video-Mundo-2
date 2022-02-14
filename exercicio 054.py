# Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas ja são maiores.
import datetime

totalmaior = 0
totalmenor = 0
for nasc in range (1,8):
    n = int(input('Digite o ano em que você nasceu? '))
    id = datetime.date.today().year - n

    if id >= 21:
      totalmaior += 1
    
    else:
      totalmenor += 1
    
print('Ao todo tem {} pessoas maiores de idade'.format(totalmaior))
print('E {} pessoas menores de idade'.format(totalmenor))
