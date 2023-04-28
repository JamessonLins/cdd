nomes=[]
senhas=[]

for c in range (2):
    nomes.append(str(input("Informe os nomes dos usuarios:").upper().lower()))
    senhas.append((input("Informe a senha dos usuarios:")))

login = str(input("Informe o login? "))
senha = (input("Informe a senha?"))
cont=0
for d in range (2):
    if login != nomes[d] and senha != senhas[d]:
         cont+=1
    else:
        print(f"logado com sucesso!")
        break
if cont == 2:
    print(f"O usurio nao foi encontrado")
print(f"Fim do programa")