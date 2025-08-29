nums = []
for i in range(5):
    valores = int(input(f"Digite o {i+1}º número: "))
    nums.append(valores)
maior = max(nums)
menor = min(nums)

print(f"Os valores digitados forma {nums}")
print(f"O maior numeros digitado foi {maior}")
print(f"O menor numero digitado foi {menor}")
print(f"A posição do maior numero é {nums.index(maior)}")
print(f"A posição do menor numero é {nums.index(menor)}")
