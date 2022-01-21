#Crie um programa que simule o funcionamento deum caixa eletrônico.
#No exercício, pergunte ao usuário qual será o valor a ser sacado
#(numero inteiro) e o programa vai informar quantas cédulas de cada
#valor serão entregues.
#Considere: 50,20,10,1

valor = int(input('Qual o valor do saque? '))
total = valor
céd=50
totalced = 0
while True:
    if total >= céd:
        total -= céd
        totalced += 1
    else:
        if totalced > 0:
             print(f'Total de {totalced} cedulas de {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd ==10:
            céd = 1
        totalced=0
        if total == 0:
            break