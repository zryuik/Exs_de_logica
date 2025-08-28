num = (int(input("Digite o primeiro número: ")),int(input("Digite o segundo número: ")),
int(input("Digite o terceiro número: ")),int(input("Digite o quarto número: ")))

print(f"Você digitou os valores {num}")

print(f"O valor 9 apareceu {num.count(9)} vezes ")

if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}ª")
else:
    print("O valor 3 não foi digitado")

print(f"Os valores pares digitados foram ", end+)
for numeros in num:
    if numeros % 2 == 0:
        print(numeros, end=' ')
