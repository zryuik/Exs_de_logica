'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado '''

from random import randint
from time import sleep
from operator import itemgetter


dados = {
    "jogador 1": randint(1,6),
    "jogador 2": randint(1,6),
    "jogador 3": randint(1,6),
    "jogador 4": randint(1,6),
    }


rank = {}
for k , v in dados.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)


rank = sorted(dados.items(), key=itemgetter(1), reverse= True)
print("== RANKING DOS JOGADORES ==")
for jogador, valor in enumerate(rank):
    print(f"{jogador+1}º lugar: {valor[0]} com {valor[1]}.")
    sleep(1)
