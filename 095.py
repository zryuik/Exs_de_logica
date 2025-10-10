'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''


time = [] # Aqui vou guardar todos os jogadores

while True:
    jogador = {} #Dicionário para um jogador
    partidas = [] #Lista com gols de cada partida
    jogador["nome"] = str(input("Nome do jogador: "))
    total_partidas = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
    for p in range(total_partidas):
        gols = int(input(f"    Quantos gols na partida {p+1}? "))
        partidas.append(gols)
    jogador["gols"] = partidas[:] #Cópia da lista
    jogador["total"] = sum(partidas) #Soma dos gols
    time.append(jogador.copy()) #Copy é importante!
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in "SN":
            break
        print('Erro! Digite apenas S ou N.')
    if continuar == "N":
        break
print("-=" * 30)
print(f"{"Cod":<5}{"Nome":<15}{"Gols":<20}{"Total":<5}")
print("-=" * 50)


for i, jogador in enumerate(time):
    print(f'{i:<5}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]:<5}')

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')      
        for i, g in enumerate(time[busca]["gols"]):
            print(f"     No jogo {i+1} fez {g} gols.")
    print("-=" * 30)
print("<<< VOLTE SEMPRE >>>")