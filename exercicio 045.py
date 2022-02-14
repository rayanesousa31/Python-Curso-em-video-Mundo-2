#Crie um programa que faça o computador jogar Jokenpô com você

import random 
import time

itens = ('Pedra', 'Papel', 'Tesoura')
escolhido = random.randint(0,2)
print( 'Eu escolho:{}'.format(itens[escolhido]))

print('''Vamos jogar JOKENPO!
[0] PEDRA 
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Escolha sua jogada:'))

print('*-----' *15)
print('O computador escolheu {}'.format(itens[escolhido]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('*-----' *15)

if escolhido == 0:
     if jogador  == 0:
          print('EMPATE!')
     elif jogador == 1:
          print('Papel ganha de pedra. Jogador vence')
     elif jogador == 2:
          print('Pedra ganha de tesoura. Computador vence')
     else:
          print('Jogada invalida')

elif escolhido == 1:
     if jogador == 0:
          print('Papel ganha de pedra.Computador vence')
     elif jogador == 1:
          print('EMPATE!')
     elif jogador == 2:
          print('Tesoura vence papel. Jogador vence')
     else:
          print('Jogada Invalida')

elif escolhido == 2:
     if jogador == 0:
          print('Pedra vence tesoura.')
     elif jogador == 1:
          print('Tesoura vence de papel')
     elif jogador == 2:
          print('EMPATE!')
     else:
          print('Jogada invalida')
