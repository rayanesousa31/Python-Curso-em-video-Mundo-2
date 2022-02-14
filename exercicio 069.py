#Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o 
#usuário quer ou não continuar. No final, mostre:
#-Quantas pessoas tem mais de 18 anos.
#-Quantos homens foram cadastrados
#-Quantas mulheres tem menos de 20 anos
quant18 = 0
quantsexom = 0
sexf = 0
while True:
    id = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M] ')).upper().split()[0]
    if id >= 18:
        quant18 += 1
    if sexo == 'Mm':
        quantsexom += 1
    if sexo == 'F' and id < 20:
        sexf += 1 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]')).upper().split()[0]
    if resp == 'N':
        break
    
print(f'Tem {quant18}  de passoas acima de 18 anos, {quantsexom} do sex masculino e {sexf} mulheres menos de 18.')
print('ACABOU')  