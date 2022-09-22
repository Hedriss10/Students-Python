from conta import Conta

 
class ContaPoupanca(Conta):
    def sacar(self):
        if self.saldo < self.valor:
            print("Saldo Insuficiente")
            