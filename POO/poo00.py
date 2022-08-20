""""
    programação orientada objeto é de grande utilidade quando,
    a demanda de code é alta, a estrutura sera mais rapida ainda
"""
from datetime import datetime


class Funcinario:

    def __init__(self, nome, sobrenome, idade, profissao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.profissao = profissao

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


    def funcionario_idade(self):
        ano_atual = datetime.now().year
        self.idade = int(ano_atual - self.idade)
        return self.idade



user1 = Funcinario('Hedris', 'Pereira', 1998, 'Developer')
user2 = Funcinario('Henrique', 'Pereira', 2000, 'SGDB')

print(user2.funcionario_idade())
