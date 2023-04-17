n = int(input('Informe o numero?\n'))

for c in range(1,n+1,1):
    impar = (c % 2) == 1
    print(f'{impar}')