''' Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno '''

def area(largura,comprimento):
    area = (largura * comprimento)
    print(f"A área de um terreno {largura} x {comprimento} é de {area:.2f} m².")

largura = float(input("Digite a largura (m): "))
comprimento = float(input("Digite o comprimento (m): "))

area(largura,comprimento)

