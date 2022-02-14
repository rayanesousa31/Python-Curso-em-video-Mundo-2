#Faça um programa que jogue PAR ou IMPAR com o computador.
#O jogo será interrompido quando o jogador PERDER,mostrando
#o total de vitórias consecutivas que ele conquistou no 
#final do jogo.

from random import randint
from time import sleep

print('Vamos jogar IMPAR ou par'),sleep(2)

cont = 0
while True:
    jogador = int(input('Digite um número '))
    comp = randint(1,10)
    jogo = comp + jogador
    opção = ' '
    while opção not in 'PI':
         opção = str(input('Você escolhe impar ou par? [I / P] ')).upper().split()[0]
    print(f'Você jogou {jogador} e o computador {comp}. Total de {jogo}')
    if opção == 'p':
        if jogo % 2 == 0:
            print('Parabéns, você venceu')
            cont += 1
        else:
             print('Você perdeu')
             break
    elif opção == 'I':
        if jogo % 2 == 1:
            print('Você venceu')
            cont += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print(f'Você venceu {cont} vezes.')

