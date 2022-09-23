from http.client import OK
import requests


class Pessoa:

    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome 
        self.dados_obetidos = False 




    def obeter_todos_os_dados(self):
        resposta = requests.get('https://casino.bet365.com/live-casino/')

        if resposta.ok:
            self.dados_obetidos = True 
            return 'CONECTADO'

        else:
            return 'ERRO 404'


