soma = cont = 0
while True:
    numero = int(input('Digite um valor (999 para parar) '))
    if numero == 999:
       break
    soma += numero
    cont += 1
print(f'Voce digitou {cont} números e a soma entre eles é de {soma}')