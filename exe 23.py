n =[]
for x in range (5):
    n.append(int(input("Informe os numeros para a lista?")))

num=int(input("Informe o numero para procurar na lista"))
cont=0
for y in range (5):
    if num == n[y]:
        cont+=1
print(cont)