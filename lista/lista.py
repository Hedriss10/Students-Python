from random import randint



lista = ['Hedris' , 'Douglas', 'Rodrigo' , 'Alexandre']


notas = [randint(5,10), randint(5,10) , randint(5,10), randint(5,10)]

for lista, notas in zip(lista, notas):
   print(f'O aluno {lista} tirou {notas}')

