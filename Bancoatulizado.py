import datetime

arquivo = open("extrato.txt", "a")
class Banco:
    def __init__(self,Num_Conta,Saldo,Agencia,Nome,TipoConta,Limite,Limite_Usado,Status=True):
        self.Num_conta=Num_Conta
        self.Saldo=Saldo
        self.Saque=0
        self.Agencia=Agencia
        self.Nome=Nome
        self.TipoConta=TipoConta
        self.Data_Retirada= datetime.datetime.now()
        self.Limite=Limite
        self.Limite_Usado=Limite_Usado
        self.Deposito= False
        self.Deposito_v=0
        self.Extrato_R=False
        self.Status = Status

    # metodo para colocar limite para cheque especial
    def AtivarLimite(self):
        self.Limite = 50
        self.Limite_Usado = self.Limite
    #metodo para desativar limite
    def DesativarLimite(self):
        if self.limite != 0:
            print("Não é possivel desativar um limite diferente de 0")
        else:
            self.limite = 0
            print("Seu limite agora está desativado!")
    #metodo para mostrar na tela o saldo
    def  Extrato(self):
        if self.Status == True:
            if self.Extrato:
                print(f"Número da conta: {self.Num_conta}, depósito de R$ {self.Deposito_v} ocorrido em: {self.Data_Retirada}")
            else:
                print(f"Número da conta: {self.Num_conta}, saque de R$ {self.Saque} ocorrido em: {self.Data_Retirada}")
        else:
            print("Não é possível consultar o extrato de uma conta desativada!")




    # metodo para atribuir valor em saldo
    def Depositar(self, valor):
        if self.Limite_Usado != 0 and self.Saldo <=0:
            valor_limite = valor = self.Saldo
            self.Saldo=0
            valor_saldo = valor_limite + self.Saldo
            self.Saldo=valor_saldo
            print(f"foi efetuado o deposito de {valor}")
            self.Deposito= True
            self.Deposito_v = valor
            print(f" caro cliente \033[34m{self.Nome}\033[0;0m você fez o deposito de \033[32m{valor}\033[0;0m e seu novo saldo é \033[32m{self.Saldo}\033[0;0m e o seu limite é de {self.Limite_Usado}")
            arquivo.write(
                f"Número da conta: {self.Num_conta}, depósito de R$ {self.Deposito_v} ocorrido em: {self.Data_Retirada}\n")
        else:
            self.Saldo += valor
            print(f"Você depositou R${valor}")
            self.Extrato_R = True
            self.Deposito_v = valor
            arquivo.write(
                f"Número da conta: {self.Num_conta}, depósito de R$ {self.Deposito_v} ocorrido em: {self.Data_Retirada}\n")

    # metodo para sacar
    def Sacar(self,valor):
        if valor <= self.Saldo:
            self.Saldo-=valor
            print(f" caro cliente \033[34m{self.Nome}\033[0;0m você fez o saque de \033[32m{valor}\033[0;0m e seu novo saldo é \033[32m{self.Saldo}\033[0;0m")
        if valor > self.Saldo:
            total = self.Saldo + self.Limite_Usado
            if valor > total:
                print(f"valor pedido {valor} é muito excedente para seu saldo ")
                arquivo.write(
                    f"Número da conta: {self.Num_conta}, depósito de R$ {self.Deposito_v} ocorrido em: {self.Data_Retirada}\n")
            else:
                self.Limite_Usado = self.Limite_Usado - (valor - self.Saldo)
                self.Saque = valor
                print(f"o valor foi aceito e seu novo saldo em conta é {valor-total} e o limite gasto foi {self.Limite_Usado-self.Limite}")
                arquivo.write(
                    f"Número da conta: {self.Num_conta}, depósito de R$ {self.Deposito_v} ocorrido em: {self.Data_Retirada}\n")

   # metodo para desativar conta
    def Desativar(self):
        if self.Status == True and self.Saldo == 0:
            print(f" Caro cliente \033[34m{self.Nome}\033[0;0m sua conta tem condições e está sendo desativa obrigado")
            self.Status = False
        else:
            print(f"Caro cliente \033[34m{self.Nome}\033[0;0m sua conta não pode ser desativada veja as regras para isso ou entre em contato com agencia")

    # metodo para verificar dados da conta como o saldo e limite
    def Verificarsaldo(self):
        if self.Status == True:
            print(f"Seu saldo atual é de: R${self.Saldo}")
            print(f"O saldo do usuario \033[34m{self.Nome}\033[0;0m é \033[32mR${self.Saldo}\033[0;0m e o limite é {self.Limite} ")
        else:
            print(f"Não é possível verificar o saldo de uma conta inativa!")

#Num_Conta,Saldo,Agencia,Nome,TipoConta,Status da conta ativada/desativada
P1= Banco(101,500,"BB","Jamesson","Poupança",0,0)
P1.AtivarLimite()
P1.Extrato()
P1.Depositar(50)
P1.Sacar(600)
P1.Depositar(50)
P1.Verificarsaldo()

