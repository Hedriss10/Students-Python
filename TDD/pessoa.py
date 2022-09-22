import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.dados_obetidos = False

    def obter_todos_os_dados(self):
        reposta = requests.get('https://docs.python.org/3/library/unittest.html')
        if reposta.ok:
            return 'CONECTADO'
        else: 
            return 'ERRO 404'