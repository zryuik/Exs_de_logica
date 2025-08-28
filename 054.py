from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8 ):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1

    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maior de idade')
print(f'E tambem tivemos {totmenor} pessoas menores de idade')
