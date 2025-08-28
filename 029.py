#escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado. a multa vai custar RS$ por cada Km acima do limite
v = float(input('A quantos Km/h ele estava: '))
multa = (v-80) * 7 #aqui eu fiz o calculo da multa subtraindo velocidade - 80 e multiplicando o que sobrou
if v > 80:
    print('MULTADO! voce excedeu o limite permitido de 80Km/h ')
    print(f'Voce deve pagar uma multa de R${multa:.2f}! ')
print('Tenha um bom dia e lembre-se de dirigir com segurança! ')    