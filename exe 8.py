n = 1
while n <= 2:
    n1 = int(input("informe o valor?\n"))
    if n1 == 0:
        print(f"o valor digitado é invalido digite outro valor")
    else:
        div = n1 / n1
        n += 1
print(f"{div}")