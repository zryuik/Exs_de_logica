#faça um programa que leia a frase pelo teclado e mostre:

#quantas vezes aparece a letra 'a'
#em que posição ela aparece a primeira vez
#em que posição ela aparece a última vez(
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind('A')+1}')