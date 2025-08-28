n = int(input('Digite um numero: '))
print(f'\nA Tabuada de {n} é: ')
for c in range(1, 11):
    resultado = n * c
    print(f'{n} x {c} = {resultado}')