'''
no python, o comportamento dos operados é definido por métedos
especificos. Vamos altera o comportamento de operadores com classes
definidas pelo o usuario.

'''


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.Y
        return Retangulo(novo_x, novo_y)



r1 = Retangulo(10, 20)
r2 = Retangulo(20, 10)
print(r3)

