class Pessoas:
    def __init__(self,nome,peso,idade,conversar=False,comendo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.conversar=conversar
        self.comendo=comendo


    def Comer(self,comida):
        # usado pra chamar o atributo que nesse caso foi o comendo
        self.comida = comida
        if self.comendo == False:
            print(f"{self.nome} va comer {self.comida}")
            self.comendo = True
        else:
            print(f"{self.nome} já esta comendo {self.comida}")

    def PararComer(self):
        if self.comendo == True:
            print(f"{self.nome} pare de comer  {self.comida}")
            self.comendo = False
    def Falar(self):
        if  self.conversar == False:
          #testar se esta comendo
          if self.comendo == True:
              print(f"{self.nome}  esta comendo {self.comida} ele nao pode falar")
          else:
              print(f"{self.nome}  pode começar uma conversar")
        else: #esta conversando
            if self.comendo==True:
                print(f"{self.nome}   não pode converasar pois esta comendo")
            else:
                print(f"{self.nome} não esta comendo  e pode conversar ")
    def PararFalar(self):
        if self.conversar == True and self.comendo == True:
            print(f"{self.nome} tem que parar de falar ")
        else:
            print(f"{self.nome} ele pode começar a falar")


#chamado de um atributo
#vars chama o dicionario da class
P1 = Pessoas("João",80,23,"",True)
P2 = Pessoas("Maria",54,19,True,)
P1.Comer("banana")
P1.PararComer()
P1.Falar()
P1.PararFalar()
P2.Comer("uva")
P2.Comer("uva")
P2.Falar()
P2.PararFalar()