n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
opcao = 0

while opcao != 6:
    print('''QUAL OPERAÇÃO VOCE DESEJA FAZER?
      
      [ 1 ] SOMA
      [ 2 ] DIVISÃO
      [ 3 ] SUBTRAÇÃO
      [ 4 ] ELEVAÇÃO
      [ 5 ] MULTIPLICAÇÃO
      [ 6 ] SAIR

''')

    opcao = int(input('Qual a opção desejada? '))

    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')

    elif opcao == 2:
        if n2 != 0:
            print(f'A divisao de {n1} e {n2} é {n1 / n2}')
        else:
            print('Syntax error!')

    elif opcao == 3:
        print(f'A subtração de {n1} - {n2} é {n1 - n2}')

    elif opcao == 4:
        print(f'{n1}  elevado a {n2} é {n1 ** n2}')

    elif opcao == 5:
        print(f'{n1} x {n2} é {n2 * n2}')
    else:
        print('Opção invalida. tente novamente!! ')
print('FIM')