class Banco:
    def __init__(self,Num_Conta,Saldo,Agencia,Nome,TipoConta,Status=True):
        self.Num_conta=Num_Conta
        self.Saldo=Saldo
        self.Agencia=Agencia
        self.Nome=Nome
        self.TipoConta=TipoConta
        self.Status = Status
    #metodo para mostrar na tela o saldo
    def  Extrato(self):
        print(f"O saldo do usuario \033[34m{self.Nome}\033[0;0m é \033[32mR${self.Saldo}\033[0;0m ")
    # metodo para atribuir valor em saldo
    def Depositar(self, valor):
        self.Saldo += valor
        print(f" caro cliente \033[34m{self.Nome}\033[0;0m você fez o deposito de \033[32m{valor}\033[0;0m e seu novo saldo é \033[32m{self.Saldo}\033[0;0m")
    # metodo para sacar
    def Sacar(self,valor):
        if valor <= self.Saldo:
            self.Saldo-=valor
            print(f" caro cliente \033[34m{self.Nome}\033[0;0m você fez o saque de \033[32m{valor}\033[0;0m e seu novo saldo é \033[32m{self.Saldo}\033[0;0m")
        else:
            print(f"caro cliente \033[34m{self.Nome}\033[0;0m saldo insuficiente para fazer a tranzação ")

    # metodo para desativar conta
    def Desativar(self):
        if self.Status == False and self.Saldo == 0:
            print(f" Caro cliente \033[34m{self.Nome}\033[0;0m sua conta tem condições e está sendo desativa obrigado")
        else:
            print(f"Caro cliente \033[34m{self.Nome}\033[0;0m sua conta não pode ser desativada veja as regras para isso ou entre em contato com agencia")

#Num_Conta,Saldo,Agencia,Nome,TipoConta,Status da conta ativada/desativada
P1= Banco(101,5000,"BB","Jamesson","Poupança")
P1.Extrato()
P1.Depositar(50)
P1.Sacar(6000)



