'''

combinations, permutations e product - itertools
combinação - ordem  não importa
permutação - ordem importa
ambos n repetem valors unicos
produto - ordem importa e repete valores unicos
'''


from itertools import combinations

roletavip = ['preto','vermelho']

for cores in combinations(roletavip, r=36):
    print(cores)
