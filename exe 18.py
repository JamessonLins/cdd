a=[]
m=[]
mult=0
for x in range(10):
    a.append(int(input("Informe os valores para a lista?")))
c = int(input("Informe um valor para multiplicar os itens da lista:"))
for y in range(10):
    mult = c * a[y]
    m.append(mult)
print(f"o valor da primeira lista é {a}",end="")
print(f"o valor multiplicado é {c}")
print(f"os valores da segunda lista é {m}")
