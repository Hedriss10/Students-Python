# fazer um sistema de cadastro usando as class
from ast import main
from distutils.log import error
from time import sleep, time
from datetime import date

class Cadastro():
    
    #construtor 
    def __init__(self, name, sobrenome, idade, profissao, datanascimento):
        self.name = name 
        self.sobrenome = sobrenome
        self.idade = idade
        self.profissao = profissao
        self.datanascimento = datanascimento
        
    
    def registro(self):
        #sistema de aprovação
        self.idade < 18



while True:
    sleep(2)
    anoverification = 2023
    try:
        print("Seja bem vindo ao programa de cadastro")
        name = input("Digite o seu nome: ")
        sobrenome = input("Digite o seu sobrenome: ")
        idade =  int(input("Digite sua idade: "))
        profissao = input("Digite sua profissao: ")
        ano = int(input("Digite o ano de nascimento completo: "))
        sleep(3)
        print("Estamos coletando o seus dados e fazendo nossa análise")
        bot = Cadastro(name=name, sobrenome=sobrenome, idade=idade, profissao=profissao,datanascimento=ano) 
        sleep(1)
        if bot.idade < int(idade):
            raise ValueError("Infelizmente você é menor de idade")
        
        resposta = ano - anoverification
        sleep(1)
        if ano > anoverification:
            print("Você está com o ano de nascimento errado")
        else:
            print(f"Você foi aprovado")
        sleep(1)
    except:
        raise ValueError("Você não digitou o formulario errado, porfavo repita!!")
    
    finally:
        print("cadastrado com sucesso na nossa empresa!!")
        print(60*"-")
   
    
    
    