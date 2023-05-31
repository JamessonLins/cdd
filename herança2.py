class Forma():
    def __init__(self,Base,Altura):
        self.Area= Base
        self.Perimetro=Altura
class Retangulo(Forma):
    def __init__(self,Base,Altura):
        super(). __init__(Base,Altura)
    def CalcularArea(self):
        calculo = (self.Area * self.Perimetro)
        print(f" Retangulo com a area de {calculo}")
    def CalcularPerimetro(self):
        calculo = 2*(self.Area*self.Perimetro)
        print(f"Retangulo com a area de {calculo}")
class Triangulo(Forma):
    def __init__(self,Base,Altura):
        super(). __init__(Base,Altura)
    def CalcularPerimetro(self,lado,lado2,lado3):
        calculo = (lado+lado2+lado3)
        print(f"o perimetro do triangulo é {calculo}")
    def CalcularArea(self):
        calculo = (self.Area * self.Perimetro)/2
        print(f"A  area do Triangulo {calculo}")

A1 = Retangulo (10,12)
A1.CalcularPerimetro()
A1=Triangulo(10,12)
A1.CalcularPerimetro(10,2,4)