preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.20
preco_final = preco - desconto

print(f"O produto com 20% de desconto custa R$ {preco_final:.2f}")

