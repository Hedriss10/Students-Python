from abc import ABC, abstractmethod

"""
    vamos criar uma conta principa, 
    contendo agencia, 
    contendo conta,
    contendo o saldo
"""

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.__agencia =  agencia 
        self.__conta =  conta
        self.__saldo  = saldo
    '''
        criando o decoratores property do meu proprio atributo,
        e repassando para o setter
    '''
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def conta(self):
        return self.__conta
    
    @property
    def saldo(self):
        return self.__saldo
    
    
    @saldo.setter
    def saldo(self, valor):
        # pegamos o saldo do usuario 
        # arquivamos na memoria 
        # e repassamos para á proxima isistance do python 
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser númerico")
        
        
    def depositar(self, valor):
        # recebmos o valor do saldo e adquerimos no depositar
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor precisa ser depositado")
        
        self.saldo += valor 
        self.detalhes() # criando a proxima func 
        
        
    def detalhes(self):
        # com a função detalhes mostramos o saldo e deposito da conta 
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')
        
        
    @abstractmethod
    def sacar(self):
        pass