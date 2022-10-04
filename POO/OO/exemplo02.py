class Cadastro():
    
    x = "Boas vindas á empresa.."
    
    
    def __init__(self, name, idade, profissao):
        self.name = name 
        self.idade = idade 
        self.profissao = profissao
        
        
    def registro(self):
        print(f'{self.name} foi cadastrado com sucesso, sabemos que você tem {self.idade} e sua {self.profissao}')
        
        
        
    @staticmethod
    def hellow(x):
        print(x + "\nSeja bem vindo caralho.....\n")
    
        
p1 = Cadastro("Hedris" , 23, "Programador")
p2 = p1.registro()
p3 = p1.hellow("Olá")

print(p3)