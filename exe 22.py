a=[]
b=[]
c=[]

t=int(input("Informe o tamanho do array pedido?\n"))

for x in range (t):
    a.append(int(input("Informe os valores para lista? ")))
for y in range (t):
    b.append(int(input("Informe os valores para lista2? ")))
for z in range(t):
    soma = a[z]+b[z]
    c.append(soma)
    print(z,c[z])
