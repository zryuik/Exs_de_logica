#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'santos'
cid = str(input(' Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

