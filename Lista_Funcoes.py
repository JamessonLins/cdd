def Somar(n1,n2):
    somar=(n1+n2)
    print(f"A soma dos valores é {somar}")
def Subtrair(n1,n2):
    subtrair=(n1-n2)
    print(f"A subtração dos valores é {subtrair}")
def Multiplicar(n1,n2):
    multiplicar=(n1*n2)
    print(f"A subtração dos valores é {multiplicar}")
def Dividir(n1,n2):
    dividir=(n1/n2)
    print(f"A subtração dos valores é {dividir}")

#return serve como o get do java para pegar dados exemplo def Somar(A,B) return A+B

def Piramide(n):
    for x in range(1,6) :
        print(f"{str(x)*x}")


def Piramide_Sequencial():
    for x in range(5):
        for y in range(x):
            print(y, end="")
        print(x, end="\n")