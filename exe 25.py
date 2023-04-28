numeros=[]
soma = 0

for x in range(4):
    numeros.append(int(input("Informe os numeros para o vetor?\n")))
for y in range(4):
    if numeros[y] % 2 != 1:
        print(f"O numero {numeros[y]} é par\n")
for z in range(4):
    maior = numeros[0]
    if numeros[z] <maior :
        print(f"o maipr numero é {numeros[z]}")
for w in range(4):
    soma = soma + numeros[w]
cont=1
media = (soma) / 10
for v in range(4):
    if numeros[v] > media:
        cont += 1
        quantidade = cont

print(f"A quantidade de numeros maiores que {media}  são  {cont}")

