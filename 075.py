num = (int(input("Digite o primeiro número: ")),int(input("Digite o segundo número: ")),
int(input("Digite o terceiro número: ")),int(input("Digite o quarto número: ")))

print(f"Você digitou os valores {num}")

print(f"O valor 9 apareceu {num.count(9)} vezes ")

print(f"o valor apareceu na {num.index(3))}ª")