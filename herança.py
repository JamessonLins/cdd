class Animal():
    def __init__(self,Nome,Cor):
        self.Nome=Nome
        self.Cor=Cor
    def EmitirSom(self):
        print(f"O {self.Nome} emitiu som e é da cor {self.Cor}")

    def comer(self):
        print(f"o {self.Nome} foi comer...")

class Gato(Animal):
    def __init__(self,Nome,Cor):
        super(). __init__(Nome,Cor)
    def EmitirSom(self):
        print(f"O {self.Nome} miou... e é da cor {self.Cor}")

class Cachorro(Animal):
    def __init__(self, Nome, Cor):
        super().__init__(Nome, Cor)
    def EmitirSom(self):
        print(f"O {self.Nome} latil ... e é da cor {self.Cor}")

class Vaca(Animal):
    def __init__(self, Nome, Cor):
        super().__init__(Nome, Cor)

v1 = Vaca("talvez","branca")
v1.comer()
v1.EmitirSom()