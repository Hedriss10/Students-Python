"""
public, protected, private

"""

class BasedeDados:

    def __int__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['cliente'] = {id: nome}

        else:
            self.dados['cliente'].updadte({id: nome})

    def listas_clitens(self):
        for id, nome in self.dados ['clientes'].items():
    def apaga_cliente(self, id):
        del self.dados['clientes'] [id]



bd = BasedeDados
bd.inserir_cliente()
bd.inserir_cliente()
bd.inserir_cliente()
bd.inserir_cliente()
