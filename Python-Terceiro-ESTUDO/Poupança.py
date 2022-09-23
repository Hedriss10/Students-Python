from classes.conta import Conta

class ContaPoupanca(conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return


        self.sado -= valor
