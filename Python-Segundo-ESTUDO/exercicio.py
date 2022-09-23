def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao("olá", 'Hedris')
saudacao("Olá", 'Henrique')



def soma(n1, n2, n3):
    print(n1 + n2 + n2)

soma(1,2,3)
soma(30,20,50)
soma(22,11,11)


def aumento_porcentual(valor, porcentual):
    return valor + (valor * porcentual /100)


ap = aumento_porcentual(50,10)
print(ap)
ap = aumento_porcentual(22,10)
print(ap)

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'Vai toma no cu'
    if  n % 10 == 0:
        return 'Vai se fuder'
    if n % 4 == 0:
        return 'Eu sou um merda'


from random import randint

for i in range(50):
    aleatorio = randint (0,50)
    print(fb(aleatorio))





