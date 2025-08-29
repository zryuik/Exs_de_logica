valores_digit = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in valores_digit:
        valores_digit.append(n)
        print("Valor adicionado... ")
    else:
        print("Valor duplicado! ")
    r = str(input("Quer continuar ? [S/N]"))
    if r in "Nn":
        break

valores_digit.sort()
print(f"Voce digitou {valores_digit}")