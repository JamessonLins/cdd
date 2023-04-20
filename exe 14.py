n = float(input("Informe o primeiro numero?\n"))
n2 = float(input("Informe o segundo numero?\n "))
opcao=0
print(''''
    1 para soma 
    2 para subtração
    3 para multiplicação
    4 para divisao 
    5 para receber novos numeros
    6 para sair do programa
''')
while opcao !=6:
    opcao=int(input(">>> Qual sua opção?"))
    if opcao == 1 :
     print(f"A soma dos valores {n} e {n2} sao {n+n2}")
    elif opcao == 2 :
        print(f"A subtracao dos valores {n} e {n2} sao {n-n2}")
    elif opcao == 3 :
        print(f"A multiplicacao dos valores {n} e {n2} sao {n*n2}")
    elif opcao == 4 :
        print(f"A divisao dos valores {n} e {n2} sao {n/n2} ")
    elif opcao == 5:
        n = float(input("Informe o primeiro numero?\n"))
        n2 = float(input("Informe o segundo numero?\n "))
    elif opcao == 6 :
        print(f"fim do programa ")
        break
