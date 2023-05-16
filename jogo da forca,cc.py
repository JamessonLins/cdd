import random
lista_P=["lapis","arara"]
lista_n=random.choice(lista_P)
tentativas=0
chances=5
letras_selecionas = []
lista_visual=["_"] * len(lista_n)
print("inico do game")
print("as regras do jogo digite uma letra por vez")
print("Você tem 5 chances depois disso o jogo acaba")
while tentativas < chances and "".join(lista_visual) != lista_n:
    letra=(input("\nDigite a primeiro letra?")).upper().lower()
    while letra in letras_selecionas:
        print(f"A letra escolhida já foi tentada")
        letra = (input("\nDigite a primeiro letra?")).upper().lower()
        letras_selecionas.append(letra)
    if letra in lista_n :
        print(f"A letra {letra} se encontra na dentro do jogo")
        for verificar in range(len(lista_n)):
            if letra == lista_n[verificar]:
                lista_visual[verificar] = letra
                print(lista_visual)
    else:
        print(f"Essa {letra} não se encontra dentro do jogo ")
        tentativas+=1
    #quantidade de tentativas
    print(f"Você ja usou {tentativas} tentativas e só resta{tentativas-chances}")

    #estado da palavra
    print(f"Estado atual da palavra")
    print(lista_visual)

    #letras usadas
    print(f"As letras que você ja tentou foi {letras_selecionas}")
    for item in letras_selecionas:
        print(item,end="")
    #finalizando
if tentativas == chances:
    print(f"\nVoce atingiu o numero maximo de chances ")
    print(f"\nGame over")
else:
    print(f"\nVoce acertou a palavra BOM JOGO")
    print(f"\nA palavra era {lista_n}")
