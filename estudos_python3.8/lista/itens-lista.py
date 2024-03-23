"""
listas
    virificação de uma lista em python para atribuir em uma programação web
    busca de um item dentro de uma lista para verificar o produto na atribuição
"""

print("Seja bem vindo á loja Hedris")

base_db = ['fusion', 'civic', 'corola', 'megane']

busca_carros = input("\nQual carro deseja buscar: \n")


if busca_carros.lower() in base_db:
    print("Está tendo em estoque")
else:
    print("não está tendo")






