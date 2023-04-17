n1 = int(input("Informe o valor da primeira nota? \n"))
n2 = int(input("Informe o valor da segunda nota? \n"))
add="S/s"
while add == "S/s":
    while n1 < 0 or n1 > 10 or n2 <0 or n2 >10:
        n1 = float(input("Informe o valor da primeira nota? \n"))
        n2 = float(input("Informe o valor da segunda nota? \n"))
        print("Os valores informados sao invalidos digite novamente")
    else:
        print("a media do aluno é: ",(n1+n2)/2 )
    add = input("Deseja cadastrar mais nota?\n")
