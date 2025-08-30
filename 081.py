valores = []

while True:
    n = int(input("Digite um valor: "))
    valores.append(n)
    c = str(input("Quer continuar? S/N: "))
    if c in "nN":
        break
print(f"Voce digitou {len(valores)} valores")
valores.sort(reverse=True)

print(f"Os valores em ordem decrescente é {valores}")


if 5 in valores:
    print("O valor 5 foi encontrado na lista")
else:
    print("O valor 5 nao foi encontrado na lista")
