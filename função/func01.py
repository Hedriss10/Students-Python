"""
function (função)
    # dry - Dont' repeat yourself.
    # Vários arguementos (xargs) indentificando o porametro
    # criar uma função que armazena números e strings (dados)
"""


"""
*args retorna lista
**kwargs retorna dicionario
Fica á dica!
"""


def agencia(**carro):
    return carro


print(agencia(marca="Palío", cor="Branco", motor=1.0, placa=1234))
print(agencia(marca="Fusca", cor="Branco", motor=1.0, placa=1234))
