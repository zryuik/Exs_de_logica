n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
opcão = 0
while opcão != 5:
      print('-=-' * 10)
      print('''   
      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa
            ''')
      print('-=-' * 10)
      opcão = int(input('Qual é a sua opção? '))
      print('-=-' * 10)
      if opcão == 1:
            soma = n1 + n2
            print(f'A soma entre {n1} + {n2} é {soma}')    
      elif opcão == 2:
            multi = n1 * n2
            print(f'A resultado de {n1} x {n2} é {soma}' )
      elif opcão == 3:
            if n1 > n2:
                  maior = n1
            else:
                  maior = n2
                  print(f'Entre {n1} e {n2} o maior valor é {maior}')
      elif opcão == 4:
            print('Informe os números novamente: ')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
      elif opcão == 5:
            print('-=-' * 10)
            print('Obrigado pela preferencia, volte sempre!')
            print('-=-' * 10)
            exit()
      else:
            print('Opção inválida. Tente novamente') 
      print('=-=' * 10) 
print('Fim do programa! Volte sempre!')