

#def divide(n1, n2):
 #   if n2 == 0:
  #      raise ValueError('n2 não pode ser 0.')
  #  return n1 / n2
#print(divide(2,0))
#except ValueError as erro:
#    print('Você esta tentando dividir por 0.')



def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
             return valor
    except ValueError:
        pass


numero = converte_numero(input('Digite outro número: '))

if numero is not none

print(numero * 5)

