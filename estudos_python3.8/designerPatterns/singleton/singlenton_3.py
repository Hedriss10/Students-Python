class Pessoa:
    def __init__(self, nome):
        self.nome = nome



    def __call__(self, x, y):
        print('Call chamado', self.nome, x + y)




p1 = Pessoa('Hedris')
p1(2, 3)
print(p1.nome)
