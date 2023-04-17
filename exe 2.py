n = int(input('Informe um numero de 1 a 12?\n'))

if n >= 1 and n <= 12:
    if n == 1:
        print(f'O valor digitado é {n} o mes correspondente a Janeiro ')
    elif n == 2:
        print(f'O valor digitado é {n} o mes correspondete a Fevereiro')
    elif n == 3:
        print(f'O valor digitado é {n} o mes correspondete a Março')
    elif n == 4:
        print(f'O valor digitado é {n} o mes correspondete a Abril')
    elif n == 5:
        print(f'O valor digitado é {n} o mes correspondete a Maio')
    elif n == 6:
        print(f'O valor digitado é {n} o mes correspondete a junho')
    elif n == 7:
        print(f'O valor digitado é {n} o mes correspondete a julho')
    elif n == 8:
        print(f'O valor digitado é {n} o mes correspondete a Agosto')
    elif n == 9:
        print(f'O valor digitado é {n} o mes correspondete a Setembro')
    elif n == 10:
        print(f'O valor digitado é {n} o mes correspondete a Outubro')
    elif n == 11:
        print(f'O valor digitado é {n} o mes correspondete a Novembro')
    else:
        print(f'O valor digitado é {n} o mes correspondete a Dezembro')
else:
    print(f'o numero digitado é invalido')
