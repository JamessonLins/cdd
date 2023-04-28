nome=[]

for  x in range(5):
    nome.append((input("Informe os nomes?")))
print(f"o nomes digitados foram {nome}")

for y in range(4,-1,-1):
    print(f"o nome na ordem inversa é {nome[y]}")
