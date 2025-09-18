matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par  = soma_coluna = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valors para [{l+1},{c+1}]: "))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
            soma_coluna += matriz[l][c]
    print()
maior = max(matriz[1])
print("-" * 30)
print(f"A soma dos valores pares é {soma_par}")
print(f"A soma da terceira coluna é {soma_coluna}")
print(f"A o maior numero da segunda linha é {maior}")