"""
    importando todo o conjunto da class conta 
    para atribuir os demais codigo 
"""

from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite
        
    @property     
    def limite(self):
        return self.__limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo Insuficiente")
            return 
        self.saldo -= valor 
        self.detalhes()