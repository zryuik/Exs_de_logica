def conta_maluca():
    numero = cont = soma = 0
    numero = int(input('Digite um numero: [9] para encerrar: '))
    while numero != 9:
        soma += numero
        cont = cont + 1
        numero = int(input('Digite um numero: [9] para encerrar '))
    print(f'Voce digitou {cont} numeros e a soma entre eles é {soma}')
    print('FIM')

conta_maluca()