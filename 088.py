from random import randint
from time import sleep


lista_jogos = []
jogo_temporario = []


print("-" * 30)
print("-" * 5, "Bem-Vindo ao gerador da sorte", "-" * 5)
print("-" * 30)


quant_jogos = int(input("Quantos jogos voce deseja criar? "))
total_sorteado = 0
while total_sorteado < quant_jogos:
    contador_numeros = 0
    while contador_numeros < 6:
        num = randint(1,60)
        if num not in jogo_temporario:
            jogo_temporario.append(num)
            contador_numeros += 1
    jogo_temporario.sort()
    lista_jogos.append(jogo_temporario.copy())
    jogo_temporario.clear()
    total_sorteado += 1
print("-" * 5,f"SORTEANDO {quant_jogos} JOGOS ", "-" * 5)
sleep(1)   

for i, j in enumerate(lista_jogos):
    print(f"Jogo {i+1}: {j}")
    sleep(0.5)

print("-" * 30)
print("-" * 5, "<BOA SORTE! >", "-" * 5)
print("-" * 30)



