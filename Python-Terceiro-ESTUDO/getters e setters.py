

class Produto:
    def __int__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (poorcentual /100 ))

   # Getter
    @property
    def preco(self):
        return self._preco


    #Setter
    @property
    def preco(self, valor):
        if isinstance(valor, str):
        valor = float(valor.replace("R$", ''))


        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self):
        self._nome =  valor

p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', "R$15")
p2.desconto(10)
print(p2.preco)

