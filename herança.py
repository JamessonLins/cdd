class Animal():
    def __init__(self,Nome,Cor):
        self.Nome=Nome
        self.Cor=Cor

    def comer(self):
        print(f"o {self.Nome} foi comer...")

class Gato(Animal):
    def __init__(self,Nome,Cor):
        super(). __init__(Nome,Cor)

    def EmitirSom(self):
        print(f"O {self.Nome} foi miando... e é da cor {self.Cor}")


class Cachorro(Animal):
    def __init__(self, Nome, Cor):
        super().__init__(Nome, Cor)

    def EmitirSomC (self):
        print(f"O {self.Nome} foi latindo... e é da cor {self.Cor}")
