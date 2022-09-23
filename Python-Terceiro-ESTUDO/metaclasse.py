'''
EM PYTHON TUDO É UM OBJETO : INCLUINDO CLASSES
METACLASSES SÃO 'CLASSES' QUE CRIAM CLASSES
TYPE E UMA METACLASSE (!!!:::///???
'''


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa cria um métedo em b_fala {name}')

        else:
            if not callable(namespace['b_fala']):
                print('b_fala precisa ser um métedo, não um atributo')




        return type.__new__(mcs, name, bases, namespace)


