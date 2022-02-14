#Melhore o jogo do DESAFIO 028, 
# onde o computador vai 'Pensar' em um número entre 
# 0 e 10. Só
#que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários
#para vencer.

from time import sleep
from random import randint
tentativa = 0
comp = randint( 0 , 10 )
print('Vamos brincar um pouco...'),sleep(3)
print('Vamos jogar um jogo de adivinhação. Entre 0 e 10, qual número você escolheria...'),sleep(3)

usuario = int(input('Digite um número de 0 a 10: '))

while usuario != comp:
    usuario = int(input('Tente novamente\n'))
    tentativa += 1
    if usuario < comp:
        print('Um pouco mais.')
    elif usuario > comp:
        print('Um pouco menos. ')
print('Parabéns! Você acertou com {} tentativas'.format(tentativa))

#------------------------------
#RESOLUÇÃO GUSTAVO GUANABARA

from time import sleep
from random import randint
palpites = 0
acertou = False
comp = randint( 0 , 10 )
print('Vamos brincar um pouco...'),sleep(3)
print('Vamos jogar um jogo de adivinhação. Entre 0 e 10, qual número você escolheria...'),sleep(3)

usuario = int(input('Digite um número de 0 a 10: '))
while not acertou:
    jogador = int (input('Qual é seu palpite?'))
    palpites += 1
    if jogador == comp:
          acertou = True
    else:
       if jogador < comp:
           print('Mais...Tente mais uma ves')
       elif jogador > comp:
           print('Menos...Tente mais uma vez')
print('Acertou com  {} tentativas. Parabéns!'.format(palpites))