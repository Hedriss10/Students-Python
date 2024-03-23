
class StringReprMixin:
    
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k , v, in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()



class formulario(StringReprMixin):
    _state = {
        'nome': 'Hedris',
        'sobrenome': 'Rocha',
        'cidade': 'Brasilia-df',
        'altura': 1.80, 
        'email': 'backtonarnia@hotmail.com',
        'cep': 73080450,
    }


    def __init__(self, telefone=None, rede_social=None):

        self.__dict__ = self._state
        self.cidade = 'Rio-de-Janeiro'
        self.sobrenome = 'Da Silva'
        self.email = 'gokublack123@gmail.com'
        
        if telefone is not None:
            self.telefone = telefone

        if rede_social is not None:
            self.rede_social = rede_social




class login(StringReprMixin):
    _state = {
        'Usuario': 'Nyckzin10',
        'senha': '*******',
    }
    
    def __init__(self, ip=None, rede=None):
        self.__dict__ = self._state
        self.senha = 'Sua senha foi revelada'

        if ip is not None:
            self.ip = ip
        

        if rede is not None:
            self.rede= rede

class localhost(StringReprMixin):
    pass

if __name__ == '__main__':
    m1 = formulario(telefone='40028922', rede_social='@niyckzin10')
    print(m1)


    m2 = login(ip='12.120.300/800', rede='8713y4372131w')
    print(m2)

    m3 = localhost()
    print(m3)