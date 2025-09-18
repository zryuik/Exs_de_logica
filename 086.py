matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):  #laço para perguntar as linhas e colunas
        matriz[l][c] = int(input(f"Digite um valor para [{l+1},{c+1}]: "))
for l in range(0,3):
    for c in range(0,3): 
        print(f"[{matriz[l][c]:^5}]", end='')
    print()