continua="s"
while continua =="s":
    numero = float(input("Informe um numero? \n"))

    if numero % 2 == 0 :
        if numero != 0:
            if numero > 0:
                print(f"o {numero} é par e positivo")
            elif numero < 0:
                print(f"o  {numero} é impar e negativo")
        else:
            print(f"O numero informado é {numero}, só aceitamos numeros diferentes de 0 ")
    else:
        if numero != 0:
            if numero >0:
                print(f"o {numero} é impar e positivo")
            elif numero <0:
                print(f"o {numero} é impar e negativo")
        else:
            print(f"O numero informado é {numero}, só aceitamos numeros diferentes de 0 ")
    continua = (input("Deseja continua?\n"))