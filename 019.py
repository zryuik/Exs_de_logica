from random import choice
pa = str(input('Primeiro aluno: '))
sa = str(input('Segundo aluno: '))
ta = str(input('terceiro aluno: '))
qa = str(input('quarto aluno: '))
lista = [pa, sa, ta, qa]
escolhido = choice(lista)
print(f'O aluno escolhido foi: {escolhido}')
