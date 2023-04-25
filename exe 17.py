notas = []
soma = 0
cont = 0
for x in range(5):
    notas.append(float(input("Informe a  nota dos alunos?")))
for y in range(5):
    soma+=notas[y]
#    print(f"A soma dos valores são {soma}")
media = soma/5
print(f"A media dos alunos são: {media}")
for z in range(5):
    if media <= notas[z]:
        cont += 1
print(f"A quantidade de alunos são {cont}")



