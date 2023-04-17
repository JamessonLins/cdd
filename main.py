n = float(input('Informe o numero para saber se é par ou impar ?\n'))

if (n == 0):
    print(f'O numero {n} é invalido boa sorte')
#divisao do programa para decidir o 0
else:
    if (n % 2) == 0:
        print(f'O numero que voce escolheu {n} é par')
    elif (n % 2) == 1:
        print(f'O numero que voce escolheu {n} é impar')
