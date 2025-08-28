pesomaior = 0
pesomenor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        pesomaior = p
        pesomenor = p
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso  < pesomenor:
            pesomenor = peso
print(f'O maior peso lido foi de {pesomaior}Kg')
print(f'E o menor peso lido foi de {pesomenor}')             
