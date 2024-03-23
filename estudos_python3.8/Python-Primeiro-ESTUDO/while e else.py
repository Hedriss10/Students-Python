'''
while/ else - aula 8
contadores
acumuladores

'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador , acumulador)

 if contador > 5:
     breakpoint()

    acumulador = acumulador + contador

    contador += 1
else:
    print('Cheguei no else.')
