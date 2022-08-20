"""
    generator expressions
    / uma forma mais rapida para listas, dicionarios e etc
    / menos memória alocada
    / valores em bytes
"""

from sys import getsizeof


list1 = []

for x in range(1000):
    list1.append(x)

print(list1)
print(getsizeof(list1))