"""
    # é uma pequena função sem nome
    # pode ter varios arguemetos mais somente uma 1 expresão
    # muito utilizada dentro de outras função
    # código mais clean
"""

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 100


print(somar(10))