#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')
    """
    Exibe a ficha de um jogador de futebol.

    Parâmetros:
    jogador (str): Nome do jogador. Valor padrão é '<desconhecido>'.
    gols (int): Número de gols marcados. Valor padrão é 0.

    A função imprime uma mensagem informando quantos gols o jogador fez.
    """

nome = input("Nome do jogador: ").strip() # Solicita o nome do jogador ao usuário e remove espaços extras
gols = input("Número de gols: ").strip() # Solicita o número de gols e remove espaços extras

if nome == "":  # Se o nome estiver vazio, define como '<desconhecido>'
    nome = "<desconhecido>"

if gols.isdigit(): # Verifica se o valor digitado para gols é um número
    gols = int(gols) # Converte para inteiro se for número
else:
    gols = 0 # Se não for número, assume 0 gols

ficha(nome,gols)  # Chama a função ficha com os dados tratados