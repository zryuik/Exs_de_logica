nome_media = {}
escola = []


for nm in range (0,1):
    nome_media["nome"] = str(input("Nome: "))
    nome_media["media"] = str(input("Média: "))
    escola.append(nome_media.copy())


    
for s in escola:
    for ap in s.values():
        print(f"Situação é igual a {escola}")
       


