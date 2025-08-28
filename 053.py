frase = (input('Digite uma frase: '))
palavras = frase.split() #eliminando espaços antes e dps com .split()
junto = ''.join(palavras) #eliminando espaços interno com join()
inverso = ''
for letra in range(len(junto) -1, -1, -1):#
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
        
print(junto, inverso)

