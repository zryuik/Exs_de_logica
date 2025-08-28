soma =  0
count = 0
for c in range(1, 7):
        num = int(input(f'digite o {c} valor: '))
        if num % 2 == 0:
                soma += num
                count += 1
print(f"Voce informou {count} números PARES e a soma foi {soma}")