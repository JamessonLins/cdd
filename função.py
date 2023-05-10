from Lista_Funcoes import *
print("""informe qual operação você que fazer entre 
                1- somar
                2- sub
                3- mult
                4- dividir
                5-sair
                """)
x=0
while True:
    x = int(input("Informe uma dessas opções acima?\n"))
    if x==5:
        break
    n1=float(input("Informe o primeiro valor?\n"))
    n2=float(input("Informe o segundo valor?\n"))
    if x == 1:
        Somar(n1,n2)
    elif x == 2:
        Subtrair(n1,n2)
    elif x == 3:
        Multiplicar(n1,n2)
    elif x == 4:
        Dividir(n1,n2)
    continuar=input("Que escolher outra opção?")




