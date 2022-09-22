def singleton(the_class):
    instace = {}
    

    def get_class(*args, **kwargs):
        if the_class not in instace:
            instace[the_class] = the_class(*args, **kwargs)
        return instace[the_class]


    return get_class


@singleton
class AppSettings:
    def __init__(self):
        print('oi')
        self.tema = 'O tema escuro'
        self.font = '20px'



@singleton
class test:
    def __init__(self):
        print('oi')



if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)


    as2 = AppSettings()
    print(as1.tema)

    t1 = test
    t2 = test