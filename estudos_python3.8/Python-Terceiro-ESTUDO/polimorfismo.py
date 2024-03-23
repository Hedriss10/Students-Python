''''
polimorfismo é o principio que permite que a classes derivada de uma mesma
superclasse tenham métedos iguais (de mesma assinatura) mas comportamentos
diferente
mesma assinatura = mesma quantidade e tipo de parâmetros
'''


from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B está flando {msg}')


class C(A):
    def fala(self, msg):
        print('C está falando {msg')


b = B()
c = C()
b.fala('UM ASSUNTO')
c.fala('OUTRO ASSUNTO')
