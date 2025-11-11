from modulos.moeda import moeda

p = float(input("Digite o preço: R$ "))
print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumentando em 10%, temos {moeda.aumentar(p)}")
print(f"Reduzindo em 13%, temos {moeda.diminuir(p)}")