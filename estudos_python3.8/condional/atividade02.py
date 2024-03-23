from random import randint


capacidade_maxima_balde = 1000

balde = 0

while balde <= capacidade_maxima_balde:
    
    
    volume = randint(90, 100)
    
    balde += volume
    
    print(f'o balde foi prennchido com {balde}mls')
    
print(f"\nO container foi preenchido e ultrapassou a capacidade maxima de {capacidade_maxima_balde}  e adcionado com balde de {balde}mls\n")    
