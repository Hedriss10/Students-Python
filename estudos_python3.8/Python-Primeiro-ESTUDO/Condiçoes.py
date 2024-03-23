
'''
condições IF, ELIF E ELSE - AULA TOP

'''
'''
if False:
    print('Verdadeiro.')
elif True:
    print("Agora é Verdadeiro")
elif False:
    print('Mais uma verdadeira')
else:
    print("Não é verdadeiro")
'''
'''
Operadores Relacionados - Continuação 

== igualdade  >maior que > maior que ou igual a < maior que ou igualdade>= <= !=

'''
'''num_1 = 2 #int
num_2 = 2 #int

expressao = (num_1 > num_2)

print(expressao)'''

nome = 'Joãozinho'
idade = """40"""
peso = 80.5
e_maior = True
idade = int(idade)

if idade > 18:
    print(f'{nome} é maior de idade.')
else:
     print(f'{nome} NÃO é maior de idade.')
