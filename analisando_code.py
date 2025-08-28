n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0 
while op != 7:
    print('-=-' * 10)
    print('''
    [ 1 ] SOMAR
    [ 2 ] DIMINUIR
    [ 3 ] MULTIPLICAR
    [ 4 ] DIVIDIR
    [ 5 ] NOVOS NUMEROS
    [ 6 ] MAIOR
    [ 7 ] SAIR DO PROGRAMA''')

    print('-=-' * 10)
    op = int(input('Qual é a sua opção? '))
    print('-=-' * 10)

    if op == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')

    elif op == 2:
        diminuição = n1 - n2
        print(f'A subtração de {n1} - {n2} é {diminuição}')

    elif op == 3:
        multiplicação = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é {multiplicação}')
    elif op == 4:
        dividir = n1 / n2
        print(f'A divisão de {n1} / {n2} é {dividir}')

    elif op == 5:
        print('Informe os números novamente: ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

    elif op == 6:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'Entre {n1} e {n2} o maior número é {maior}')

    elif op == 7:
        print('Obrigado pela preferencia ')
  

    else:
        print('Opção invalida. tente novamente')

print('Fim do programa. Volte sempre!')