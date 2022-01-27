#Refaça o desafio 035 dos triangulos,
#acrescentando o recurso de mostrar que 
# tipo de triangulo será formado:
#equilatero:todos os lador iguais
#isosceles: dois lados iguais
#escaleno:todos os lados diferentes


r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Treceio segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print('Os segmenos acima podem formar um triangulo')
    if r1 == r2 and r1 == r3 and r2 == r3:
       print('Triangulo equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3 or r2 == r1:
       print('Isosceles')
    elif r1 != r2 and r3 != r2 and r3 != r1 :
       print('Escaleno')
else:
    print('Não se pode formar triangulo com essas metricas')


