#desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem, cobrando r$0,50 por km para viagens de ate 200km e r$045 para viagens mais longas
distancia = float(input('Digite a distancia dessa viagem: '))
print(f'Voce esta prestes começar uma viagem de {distancia} Km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da sera de R$ {preco:.2f}')