

class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index =  0

    def add(self,valor):
        self.__items.append((valor))

    def __iter__(self):
        return

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item 1


    def __str__(self):
        return f'{self.__class__.__name__}'



if __name__ == "__main__"
    lista = MinhaLista
    lista.add("Hedris")
    lista.add("Rocha")


