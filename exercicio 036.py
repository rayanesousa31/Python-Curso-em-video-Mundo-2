#Escreva um programa para aprovar o empréstimo bancário
#para a compra de uma casa. O programador vai perguntar o 
#valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 
#30% do salário ou então o emprestimo será negado

casa = float(input('Qual o valor da casa a ser comprada? '))
sal = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos meses: '))

prestacao = casa / tempo
sal1 = sal * (30/100)
#prestaçao  = casa / (anos * 12) caso fosse feito em anos (e não em meses)
if prestacao > sal1:
    print('O valor da prestação fica acima de 30% de seu salário, portanto seu emprestimo foi negado!')

else:
    print('Emprestimo aceito! O valor do seu emprestimo fica R${} em {} meses'.format(prestacao,tempo))