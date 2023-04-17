'''n=1
soma=0
while n <= 10:
    n1 = float(input("informe os valores a ser salvos ?\n"))
    soma = soma + n1
    n = n+1
    media = (soma)/10
print(f'{media}')'''

#lembrar de fazer com grande escala
n=1
soma=0
n1 =int(input("informe o valor de quantas vezes vai somar e o valor final do dividendo da media?\n"))
while n <= n1:
    n2 = float(input("informe os valores a ser salvos ?\n"))
    soma = soma + n2
    n = n+1
media = (soma) / n1
print(f' A media final foi {media}')