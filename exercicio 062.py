#Melhore o DESAFIO 61, perguntando para o usuário se 
# ele quer mostrar mais alguns termos. 
# O programa encerra quando ele 
# disser que quer mostrar 0 termos.

n = int(input('Digite um numero: '))
razao = int(input('Digite uma razao: '))
termo = n
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    #total+= 1
    while cont <= total:
        print(' {}'.format(termo), end=' ')
        termo += razao
        cont+= 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar? '))
print('O total de termos foi: {}'.format(total))
print(  'Fim')

    