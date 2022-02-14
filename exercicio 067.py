#Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido quando
#o número solicitado for negativo.


#n = int(input('Digite um valor para ver a tabuada:'))
while True:
    n = int(input('Digite um valor:'))
    if n < 0:
        
        break
    for c in range (1,11):
        mult = n * c
        print(f'{n} x {c:2} = {mult:2}')
print('Programa encerrado')
    


    
    
        