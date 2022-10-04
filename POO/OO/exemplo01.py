# classe cadastro 


class Cadastro():
    #indep. de instancias
    raca = "Preto"
    
    #contrutor 
    def __init__(self):
        self.name = "Hedris"
        self.sobrenome = "Rocha Pereira"
        self.idade =  23
        self.profissao = "Programador"
        
    
    

p1 = Cadastro()
print(p1.idade)
