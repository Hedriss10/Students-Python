""""
    list compreheinson
        mais simples de se escrever
        utilizado quando você precisa criar uma lista a parti de uma existente
        [expressão for iten in itens]

"""


frust1 = ['abacate', 'banana', 'morango', 'laranja', 'melão']

frust2 = [iten for iten in frust1 if 'a' in iten]

#for itens in frust1:
#    if 'b' in itens:
#        frust2.append(itens)

print(frust2)