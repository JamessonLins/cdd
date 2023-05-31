class Atleta():
    def __init__(self,Peso,Aposentado=True,Aquecido=True):
        self.Peso=Peso
        self.Aposentado=Aposentado
        self.Aquecido=Aquecido

    def Aposentar(self):
        if self.Aposentado == True:
            print(f"O atleta se encontra aposentado")
        else:
            print(f"O atleta esta em condições de continuar atuando")
    def Aquecer(self):
        if self.Aquecido == True and self.Aposentado == False:
            print(f"O atleta se encontra pronto e aquecido")
        elif self.Aquecido == False and self.Aposentado== False:
            print(f"O atleta não esta aquecido va aquecer")
        elif self.Aquecido == False and self.Aposentado == True:
            print(f"Atleta aposentado va descansar ")
        elif self.Aquecido == True and self.Aposentado == True:
            print(f"Atleta aposentado va descansar ")
class Nadador(Atleta):
    def __init__(self, Peso, Aposentado):
        super().__init__(Peso, Aposentado)

    def Nadar(self):
       if self.Aquecer == True and self.Aposentado == False:
            print(f"o atleta esta hapito a nadar")
            print(f"o atleta esta nadando")
       elif self.Aquecer == False and self.Aposentado == False:
            print(f"O atleta não esta aquecido va aquecer pra nadar")
       elif self.Aquecido == False and self.Aposentado == True:
           print(f"Atleta esta aposentado va descansar ")
       elif self.Aquecido == True and self.Aposentado == True:
           print(f"Atleta esta aposentado va descansar ")


class Ciclista(Atleta):
    def __init__(self, Peso, Aposentado):
        super().__init__(Peso, Aposentado)

    def Pedalar(self):
        if self.Aquecer == True and self.Aposentado == False:
            print(f"o atleta esta hapito a pedalar")
            print(f"o atleta esta pedalando")
        elif self.Aquecer == False and self.Aposentado == False:
            print(f"O atleta não esta aquecido va aquecer pra pedalar")
        elif self.Aquecido == False and self.Aposentado == True:
            print(f"Atleta esta aposentado va descansar ")
        elif self.Aquecido == True and self.Aposentado == True:
            print(f"Atleta esta aposentado va descansar ")


class Corredor(Atleta):
    def __init__(self, Peso, Aposentado):
        super().__init__(Peso, Aposentado)

    def Corre(self):
        if self.Aquecer == True and self.Aposentado == False:
            print(f"o atleta esta hapito a correr")
            print(f"o atleta esta nadando")
        elif self.Aquecer == False and self.Aposentado == False:
            print(f"O atleta não esta aquecido va aquecer pra correr")
        elif self.Aquecido == False and self.Aposentado == True:
            print(f"Atleta esta aposentado va descansar ")
        elif self.Aquecido == True and self.Aposentado == True:
            print(f"Atleta esta aposentado va descansar ")

class Triatleta(Corredor,Nadador,ConnectionError):
    def __init__(self, Peso, Aposentado):
        super().__init__(Peso, Aposentado)
