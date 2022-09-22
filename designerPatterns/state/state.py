"""
O padrão de projeto State é um padrão comportamental 
que tem a itenção de permitir um objeto a mudar 
seu comportamento quando o seu estado interno muda.
O objeto parecera ter mudado a class
"""

from __future__ import annotations
from abc import ABC, abstractmethod


#---classe----!
"""
Class de ordem do pedido
"""
class Order:
    """---CONTENT---"""
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject

#----ordenstate---!

"""
Ordem statica!!
"""
class OrderState(ABC):

    def __init__(self, Order):
        self.Order = Order
        


    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass


    @abstractmethod
    def reject(self) -> None: pass





#----pagamentos pendentes----!
class PaymentPending(OrderState):

    def __init__(self, Order):
        self.Order = Order
        
    
    def pending(self) -> None:
        print('Pagamento já pendente, não posso fazer nada.')
   
    def approve(self) -> None:
        self.Order.state = PaymentAproved(self.Order)
        print('Pagamento Aprovado..')

    def reject(self) -> None: 
        self.Order.state = PaymentReject(self.Order)
        print('Pagamento Reprovado')


#------pagamentos aprovados-----!
class PaymentAproved(OrderState):

    def __init__(self, Order):
        self.Order = Order
        
    
   
    def pending(self) -> None: 
        self.Order.state = PaymentPending(self.Order)
        print('Pagamento Pendente')
   
    def approve(self) -> None:
        print('Pagamento já aprovado, não posso fazer nada.')
    
    def reject(self) -> None:
        self.Order.state = PaymentReject(self.Order)
        print('Pagamento Recusado')


#------pagamentos rejeitados-----!
class PaymentReject(OrderState):

    def __init__(self, Order):
        self.Order = Order
        
  
    def pending(self) -> None:
        print('Pagamento recusado não vou move para pendente')
   
    def approve(self) -> None:
        print('Pagamento recusado, não vou recusa novamente')
    
    def reject(self) -> None:
        print('Pagamento recusado, não vou recusa novamente')




if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()