def area(largura, comprimento):
    a = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {a}m²")


print("Controle De Terrenos")
print("-" * 20)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)
