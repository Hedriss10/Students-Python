'''
expresão lambda
'''



lista = [
    ['P1',13],
    ['P2',6],
    ['P3',3],
    ['P4',11],
    ['P5',20],
]


print(sorted(lista, key=lambda i: i[1],reverse=True))
print(lista)