n = int(input('informe o numero para fazer a tabuada?\n'))
mult = 0
for i in range (0,11,1):
    mult= n*i
    print(f'A tabuada de {n} * {i} é {mult}')