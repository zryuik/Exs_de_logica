''' Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. '''
import utils
jogador = {}
partidas = []

jogador["nome"] = input("Nome do jogador: ")
total_partidas = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))

for i in range(total_partidas):
    gols = int(input(f"Quantos gols ele fez no jogo {i+1}? "))
    partidas.append(gols)
    
jogador["gols"] = partidas

jogador["total"] = sum(partidas)

utils.funçao_linha()
print(jogador)
utils.funçao_linha()


for k, v  in jogador.items():
    print(f"O campo {k} tem valors {v}")

utils.funçao_linha()
print(f"O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.")
utils.funçao_linha()

for i, v in enumerate(jogador["gols"]):
    print(f"Na partida {i}, fez {v} gols.")
print(f"Foi um total de {jogador["total"]} gols.")

utils.funçao_linha()