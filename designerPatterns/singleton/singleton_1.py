



class AppSettings:
    _instace = None 



    def __new__(cls, *args, **kwargs):
        if not cls._instace:
            cls._instace = super().__new__(cls, *args, **kwargs)
            return cls._instace



    def __init__(self):
        self.tema = 'O tema preto'
        self.font = '10px'




if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)
  
  
    as2 = AppSettings() 
    print(as1.tema)