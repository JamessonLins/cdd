n1=int(input("Informe um numero ? \n"))
n2=int(input("Informe um numero ? \n"))
n3=int(input("Informe um numero ? \n"))
maior = n1
menor = n2

if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3
elif n1 < menor:
    menor=n1
elif n3< menor:
    menor= n3

print(f"O maior valor é {maior} e o menor é {menor}")
