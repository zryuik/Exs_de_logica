from datetime import date
nascimento = int(input('Digite o ano em que voce nasceu: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'A sua idade é {idade} ')
if idade <= 9 :
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')