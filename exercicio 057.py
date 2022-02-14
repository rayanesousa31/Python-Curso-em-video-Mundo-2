#Faça um programa que leia o sexo de uma pessoa
#mas só aceite os valores M ou F . Caso esteja errado
#peça a digitação novamente até ter um valor correto
sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0]

while sexo  not in 'MmFf' :
    sexo = str(input('Dados Inválidos')).upper().strip() [0]
    
print('Sexo {} registrado co sucesso'.format(sexo))
    
