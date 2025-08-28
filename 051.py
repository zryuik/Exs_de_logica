print('10 TERMOS DE UMA PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(10):
    termo = primeiro +i * razao
    print(termo, end=' → ')
print('FIM')