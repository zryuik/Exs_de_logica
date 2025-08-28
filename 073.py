brasileirao = ('FLAMENGO', 'PALMEIRAS', 'BRAGANTINO', 'FLUMINENSE', 'BAHIA', 'CEARÁ', 'CRUZEIRO', 'CORINTHIANS', 'INTERNACIONAL',
    'SÃO PAULO', 'BOTAFOGO', 'VASCO', 'JUVENTUDE', 'MIRASSOL', 'FORTALEZA', 'ATLÉTICO-MG', 'VITÓRIA', 'GRÊMIO', 'SANTOS', 'SPORT')

print('Os cinco primeiros colocados são: ')
for tabela in range (5):
    print(f'{tabela + 1}º Lugar {brasileirao[tabela]}', )

print('Os quatro ultimos colocados da tabela são: ')    
for tabela in range (16,20):
    print(f'{tabela + 1}º Lugar {brasileirao[tabela]}', )

print('Em ordem alfabetica fica: ')
print(sorted(brasileirao))

while True:
    tab = str(input('Qual time voce deseja consultar a posição? ')).strip().upper()
    if  tab in brasileirao:
        print(f'O time {tab} esta na posição {brasileirao.index(tab) + 1}º')
        break
    print('Opção Invalida. tente novamente! ')
print('FIM')