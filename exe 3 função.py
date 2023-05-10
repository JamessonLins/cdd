texto="O rato roeu a roupa do rei de Roma".upper().lower()
cont=0
for x in texto:
    if x in "aeiouAEIOU":
        cont+=1
    print(cont)