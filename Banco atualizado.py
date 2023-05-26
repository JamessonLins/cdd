class Banco:
    def __init__(self,Num_Conta,Saldo,Agencia,Nome,TipoConta,Limite,Limite_Usado,Status=True):
        self.Num_conta=Num_Conta
        self.Saldo=Saldo
        self.Agencia=Agencia
        self.Nome=Nome
        self.TipoConta=TipoConta
        self.Limite=Limite
        self.Limite_Usado=Limite_Usado
        self.Status = Status

    # metodo para colocar limite para cheque especial
    def AtivarLimite(self):
        self.Limite = 50

    # metodo para criar um saldo colocando o limite que é o cheque especial
    #def SaldoFinal(self):

    #metodo para mostrar na tela o saldo
    def  Extrato(self):
        print(f"O saldo do usuario \033[34m{self.Nome}\033[0;0m é \033[32mR${self.Saldo}\033[0;0m e o limite é {self.Limite} ")
    #observaçao colocar o metodo de data no extrato e colocar o um arquivo texto para ser manipulado e guardar a informação "if open"

    # metodo para atribuir valor em saldo
    def Depositar(self, valor):
        self.Saldo += valor
        print(f" caro cliente \033[34m{self.Nome}\033[0;0m você fez o deposito de \033[32m{valor}\033[0;0m e seu novo saldo é \033[32m{self.Saldo}\033[0;0m")
    # metodo para sacar
    def Sacar(self,valor):
        if valor <= self.Saldo:
            self.Saldo-=valor
            print(f" caro cliente \033[34m{self.Nome}\033[0;0m você fez o saque de \033[32m{valor}\033[0;0m e seu novo saldo é \033[32m{self.Saldo}\033[0;0m")
        elif valor > self.Saldo:
            self.Saldo-=valor
            if self.Saldo < 0:
                self.Saldo += self.Limite
                self.Limite_Usado =  self.Limite_Usado - self.Limite
                print(f"esta devendo {self.Limite_Usado} do saldo de {self.Limite}")

        else:
            print(f"caro cliente \033[34m{self.Nome}\033[0;0m saldo insuficiente para fazer a tranzação ")



    # metodo para desativar conta
    def Desativar(self):
        if self.Status == True and self.Saldo == 0:
            print(f" Caro cliente \033[34m{self.Nome}\033[0;0m sua conta tem condições e está sendo desativa obrigado")
            self.Status = False
        else:
            print(f"Caro cliente \033[34m{self.Nome}\033[0;0m sua conta não pode ser desativada veja as regras para isso ou entre em contato com agencia")



#Num_Conta,Saldo,Agencia,Nome,TipoConta,Status da conta ativada/desativada
P1= Banco(101,500,"BB","Jamesson","Poupança",0,0)
P1.Extrato()
P1.AtivarLimite()
P1.Extrato()
P1.Sacar(560)
