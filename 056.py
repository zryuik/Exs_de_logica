somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'mM':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos')
print(f' O homem mais velho tem {maioridadehomem}, e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos: ')