#Desenvolva uma lógica que leia o peso e altura de uma pessoa,
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#abaixo de 18.5:abaixo do peso
#entre 18.5 e 25: peso ideal
#25 ate 30:sobrepeso
#30 ate 40: obesidade
#acima de 40: obesidade morbida


peso = float(input('Nos informe seu peso: '))
altura =  float(input('Nos informe sua altura: '))

IMC = peso / altura ** 2
#print(IMC)

if IMC >= 18.5  and  IMC <25:
        print('Seu IMC é {:.1f} e esta peso ideal'.format(IMC))

elif IMC >= 25 and IMC <30:
    print('Seu IMC é {:.1f} e esta no sobrepeso'.format(IMC))   

elif IMC >= 30 and IMC <40:
    print('Seu IMC é {:.1f} e esta na obesidade'.format(IMC))

elif IMC >= 40:
    print('Seu IMC é {:.1f} e esta na obesidade morbida'.format(IMC))

else:
    print('Seu IMC é {:.1f} e esta abaixo do peso'.format(IMC))