soma = 0
cont = 0
#recebe = int(input('Digite um numero: ')) #essa linha e para caso eu quisesse solicitar o valor 
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont +=  1
        soma +=  numero
print(f'A soma de todos os {cont} solicitados é {soma}')