a=int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))
c=int(input("Digite o terceiro número: "))
maior = c
menor = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
if b < c and b < a:
    menor = b
if a < c and a < b:
    menor = a

print(f" o menor número digitado foi {menor}")
print(f" o maior numero digitado foi {maior}")


