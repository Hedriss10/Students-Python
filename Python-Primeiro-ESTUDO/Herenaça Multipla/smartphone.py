from Eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin)
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conetar(self):
        if not self ligado:
            info = f'{self._nome} não está ligado'
            print(info)
            self.log_error(info)
            return

        if self.conectado:
            error =  f'{self._nome} Já está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} ESTÁ CONECTADO.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado
        erro = f'{self._nome}Não está conectado'
        print(erro)
        self.log_error(error)
        return

        info = f'{self._nome} Foi ligado com sucesso.'
        print(info)
        self.log_error(info)
        self.conectado = False


