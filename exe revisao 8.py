eleitores=int(input("Informe a quantidade de eleitores?\n"))
votos_brancos=int(input("Informe a quantidade de votos brancos?\n"))
votos_nulos=int(input("Informe a quantidade de votos nulos?\n"))
votos_validos=int(input("Informe a quantidade de votos validos?\n"))

cal_vb= (votos_brancos/eleitores)*100
cal_n= (votos_nulos/eleitores)*100
cal_validos= (votos_validos/eleitores)*100

print(f"o numero de votoso validos foram {votos_validos}",end="% -> ")
print(f"o numero de votoso brancos foram {votos_brancos}",end="% -> ")
print(f"o numero de votoso nulos foram {votos_nulos}",end="% -> ")