#A confederação nacional de natação precisa de um programa 
#que leia o ano de nascimento de um atleta e mostre sua 
#categoria, de acordo com a idade:
#até 9 anos  : MIRIM
#até 14 anos: INFNTIL
#até 19 anos: JUNIOR
#até 20 anos: SENIOE
#ACIMA: MASTER

import datetime

nome = str(input('Qual o nome do candidato? '))
ano = int(input('Qual o ano de nascimento do candidato? '))

candidato =  datetime.date.today().year - ano

if candidato < 9 :
   print('{} tem {} anos e esta na categoria MIRIM!'.format(nome,candidato))
if candidato >= 9 and candidato < 14:
    print('{} tem {} anos e esta na categoria INFANTIL!'.format(nome,candidato))
if candidato == 14 and candidato < 19:
    print('{} tem {} anos e esta na categoria JUNIOR!'.format(nome,candidato))
if candidato == 19 and candidato == 20:
    print('{} tem {} anos e esta na categoria SENIOR!'.format(nome,candidato))
if candidato > 20:
    print('{} tem {} anos e esta na categoria MASTER!'.format(nome,candidato))
else: 
    print('{} Boa sorte!'.format(nome))