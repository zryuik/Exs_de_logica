numero = cont = soma = 0
numero = int(input('Digite um numero: [999 para parar]: '))
while numero != 999:    
    soma += numero
    cont += 1 
    numero = int(input('Digite um numero: [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
#print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - 999}') tem como fazer desse jeito e do jeito da linha de cima