n=1
senha=2121
cont=0
while n <= 3:
    n1 = int(input("Informe a senha:\n"))

    if n1 == senha:
        print(f"senha correta Bom dia")
        break
    else :
        print(f"senha errada tente de novo")
        cont = cont + 1
        breakpoint(cont==3)
if cont==3:
    print(f"Numero de vezes ecedidas sua senha esta bloqueada")
