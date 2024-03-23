from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '&Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome}, não pode falar comendo!')
            return
        if self.falando:
            print(f'{self.nome}. Já está falando!')
            return
        print(f'{self.nome}, Está falando sobre {assunto}.')
        self.falando = True

    def para_falar(self):
        if not self.falando
            print(f'{self.nome}, Não está falando!')
            return
        print(f'{self.nome}, Parou de falar!')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome}, Não pode comer falando!')
            return
        if self.falando:
            print(f'{self.nome}, Já esta comendo ')
            return
        print(f'{self.nome}, está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.comendo}, Não está comendo')
            return

        print(f'{self.nome}, parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade





