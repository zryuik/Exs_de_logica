from datetime import date
ano = int(input('Que ano quer analisar? colocque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} é BISSEXTO ')
else:
    print(f'O Ano {ano} não é BISSEXTO')