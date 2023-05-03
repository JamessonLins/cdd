continua="s"
while continua =="s":
    numero = float(input("Informe um numero? \n"))

    if numero != 0:
        if numero >0:
            print(f"o numero {numero} é positivo")
        else:
            print(f"o numero {numero} é negativo")
    else:
        print(f"O numero informado é {numero}, só aceitamos numeros diferentes de 0 ")
    continua = (input("Deseja continua?\n"))