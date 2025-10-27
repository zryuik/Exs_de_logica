#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep

cores = (
    '\033[m',          # 0 - sem cor
    '\033[0;30;41m',   # 1 - vermelho
    '\033[0;30;42m',   # 2 - verde
    '\033[0;30;43m',   # 3 - amarelo
    '\033[0;30;44m',   # 4 - azul
    '\033[0;30;45m',   # 5 - roxo
    '\033[7m'          # 6 - branco invertido
)


def ajuda(com):
    titulo(f"Acessando o manual do comando \"{com}\"", 4)
    print(cores[6], end="")
    help(com)
    print(cores[0], end="")
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end="")
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(cores[0], end="")
    sleep(1)


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        titulo("ATÉ LOGO", 1)
        break
    else:
        ajuda(comando)
