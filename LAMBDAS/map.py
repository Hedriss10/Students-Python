"""
    map function
    ultilizado com listas
    aplica função á um iterable, por item (list, tuple, dic )
"""


list1 = [10, 30, 40, 50]


def mult(x):
    return x * 2


list2 = map(mult, list1)

print(list(list2))

