#crie um programa que leia dois valores
#e mostre um menu na tela:
#[1] somar
#[2]multiplicar
#[3]maior
#[4]novos numeros
#[5] sair do programa
#Seu programa devera realizar a operação solicitada e cada caso.

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
maior = 0
menor = 0
opcao = 0
print('Os números escolhidos foram: {} e {}'.format(v1,v2))
while opcao != 5:
      print('''Escolha uma das opções abaixo:
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NUMEROS
      [5] SAIR DO PROGRAMA''')
      opcao = int(input('Sua opção é: '))
      if opcao == 1:
        somar = v1 + v2
        print('A soma dos números {} e {} é: {}'.format(v1,v2,somar))
      elif opcao == 2:
        mult = v1 * v2
        print('A multiplicação dos números {} e {} é: {}'.format(v1,v2,mult))
      elif opcao == 3:
           if v1 > v2:
                maior = v1
           else:
                maior = v2
           print('O número maior é {}'.format(maior))
      elif opcao == 4:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro numero: '))
      
      elif opcao == 5:
            print('Saindo do programa')
      else:
          print('Opçao inválida')
print('Saindo do programa')



