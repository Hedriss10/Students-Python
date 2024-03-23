# positivos  [012345678]

#texto        ='Pyhton s2'

#print( texto[5] )
'''
while em python - aula 7
ultizando para realizar acções enquanto
uma condição for verdadeira

Requisitos entender condições e operadores

'''

#while True: # loop infinito
   # nome = input("Qual é o seu nome")
    #print(f'Olá {nome}!')

##x = 0
#while x < 15:
 #   if x == 3:
 #       x == x + 1
#        break # break para finalizar ou continue para pular

  #  print(x)
# = x + 1
#print('Acabou !')

#x = 0 # coluna
#while x < 31:
#    y = 0 # linha
#    while y < 15:
#       print(f'X vale {x} e Y vale {y}')
#        y += 1
#       x += 1 # x = x +1
#
#print('Gire a roleta denovo')


while True:
    print()
    num_1 = input('digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue
    # + - / *

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)






