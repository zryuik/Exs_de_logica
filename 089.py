ficha = []
while True:
    nome = str(input("Nome: "))
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome,[nota_1, nota_2],media])
    resposta = str(input("Quer continuar? [S/N] "))
    if resposta in "nN":
        break
print("-" * 26)


print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")


print("-" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-"*35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando")
        break
    elif opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<< VOLTE SEMPRE >>>")


