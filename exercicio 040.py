#Crie um programa que leia duas notas de alunos e calcule sua média,
#mostrando uma mensagem no final, de acordo com a media atingida:
#-Média abaixo de 5.0:REPROVADO
#-Média entre 5.0 e 6.9:RECUPERAÇÃO
#-Média 7.0 ou superior:APROVADO

n1 = float(input('Digite sua primeira nota : '))
n2 = float(input('Digite a segunda nota: '))


med = (n1 + n2)/2

if med >= 7.0:
    print('Sua média é {}. Parabéns você esta \033[1;36mAPROVADO\033[m'.format(med))
elif med == 5.0 <=6.0:
    print('Sua média é {}. Você esta de \033[1;33mrecuperação\033[m'.format(med))
else:
    print('Sua média é {}. Você esta \033[1;31mREPROVADO5\033[m'.format(med))